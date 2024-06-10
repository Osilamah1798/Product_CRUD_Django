import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Product
from django.views.decorators.csrf import csrf_exempt

def get_products(request):
    if request.method == 'GET':

        product = Product.objects.all()
#convert query set called product to product list
        product_list = list(product.values())

        print(product.values())
    
        return JsonResponse({"Message":"Get products route is active",
                             "data":product_list})
    else:
        return JsonResponse({"ERROR!!":"Invalid Method"}, status = 405)

@csrf_exempt
def add_products(request):
    if request.method == 'POST' :
        #Model syntax for adding products
        
        json_data = request.body.decode('utf-8')
        data_dict = json.loads(json_data)

        # Product.objects.create(
        #     name = data_dict["name"],
        #     image_url =data_dict["image_url"],
        #     description = data_dict["description"],
        #     type = data_dict["type"],
        #     brand =data_dict["brand"],
        #     price = data_dict["price"],
        #     available = data_dict["available"]
        # )
#Extract the product name from the data 
        product_name = data_dict.get("name")
#Check if a product with the given name already exists
        existing_product = Product.objects.filter(name=product_name).first()

        if existing_product:
                
#If the product exists, reyurn a  message indicating so
                return JsonResponse({"Message":"Product with this name already exists"})
        else:

            Product.objects.create(**data_dict)

        # print(user)

        return JsonResponse({"Message":"Post added sucessfully"})
    
    else:
        return JsonResponse({"ERROR!!":"Invalid Method"}, status = 405)
#First Trial    
# @csrf_exempt
# def update_products(request):
#     if request.method == 'PUT':
#         json_data = request.body.decode('utf-8')
#         data_dict = json.loads(json_data)

#         product_name = data_dict.get("name")
#         existing_product = Product.objects.filter(name=product_name).first()

#         if existing_product:
#             existing_product.image_url = data_dict.get("image_url", existing_product.image_url)
#             existing_product.type = data_dict.get("type", existing_product.type)
#             existing_product.brand = data_dict.get("brand", existing_product.brand)
#             existing_product.price = data_dict.get("price", existing_product.price)
#             existing_product.description = data_dict.get("description", existing_product.description)
#             existing_product.available = data_dict.get("available", existing_product.available)
#             existing_product.save()
            
#             return JsonResponse({"Message": "Product updated successfully"})
#         else:
#             return JsonResponse({"Message": "Product with this name does not exist"})
#     else:
#         return JsonResponse({"ERROR": "Invalid Method"}, status=405)


        


       

        



#Second Trial

# @csrf_exempt
# def update_products(request):
#     if request.method == 'PUT':
#         json_data = request.body.decode('utf-8')
#         data_dict = json.loads(json_data)
        
#         product_id = data_dict["id"]
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return JsonResponse({"error": "Product not found"}, status=404)
        
#         # try:
#         #         price = float(data_dict["price"])
#         # except ValueError:
#         #         return JsonResponse({"error": "Invalid value for 'price'"}, status=400)
        

#         product.name = data_dict["name"]
#         product.image_url =data_dict["image_url"]
#         product.description = data_dict["description"]
#         product.type = data_dict["type"]
#         product.brand =data_dict["brand"]
#         product.price = data_dict["price"]
#         product.available = data_dict["available"]
#         product.save()
        

#         return JsonResponse({"Message":"Changes have been made to the product"})
        
#     else:
#         return JsonResponse({"ERROR!!":"Invalid Method"}, status = 405)



#Third Trial
# @csrf_exempt
# def update_products(request):
#     if request.method == 'PUT':
#         try:
#             json_data = request.body.decode('utf-8')
#             data_dict = json.loads(json_data)
            
#             # Validate required fields
#             required_fields = ["id", "name", "image_url", "description", "type", "brand", "price", "available"]
#             for field in required_fields:
#                 if field not in data_dict:
#                     return JsonResponse({"error": f"'{field}' is required"}, status=400)
            
#             # Fetch the product by ID
#             product_id = data_dict["id"]
#             try:
#                 product = Product.objects.get(id=product_id)
#             except Product.DoesNotExist:
#                 return JsonResponse({"error": "Product not found"}, status=404)
            
#             # Convert numeric fields
#             try:
#                 price = float(data_dict["price"])
#             except ValueError:
#                 return JsonResponse({"error": "Invalid value for 'price'"}, status=400)
            
#             available = data_dict["available"]
#             if isinstance(available, str):
#                 available = available.lower() in ['true', '1', 'yes']

#             # Update the product fields
#             product.name = data_dict["name"]
#             product.image_url = data_dict["image_url"]
#             product.description = data_dict["description"]
#             product.type = data_dict["type"]
#             product.brand = data_dict["brand"]
#             product.price = price
#             product.available = available
#             product.save()
            
#             return JsonResponse({"message": "Product has been updated successfully"}, status=200)
        
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
    
#     else:
#         return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def update_products(request, id):
    if request.method == 'PUT':
        try:
            json_data = request.body.decode('utf-8')
            data_dict = json.loads(json_data)
            
            # Fetch the product by ID from the URL
            try:
                product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
            
            # Update the product fields
            product.name = data_dict.get("name", product.name)
            product.image_url = data_dict.get("image_url", product.image_url)
            product.description = data_dict.get("description", product.description)
            product.type = data_dict.get("type", product.type)
            product.brand = data_dict.get("brand", product.brand)
            product.price = data_dict.get("price", product.price)
            product.available = data_dict.get("available", product.available)
            product.save()
            
            return JsonResponse({"message": "Changes have been made to the product"}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def delete_products(request, id):
    if request.method == 'DELETE':
        try:
            # Fetch the product by ID
            try:
                product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
            
            # Delete the product
            product.delete()
            
            return JsonResponse({"message": "Product has been deleted successfully"}, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
