from django.db import transaction
from django.shortcuts import render
from .models import Product

@transaction.atomic
def create_product(request):
    if request.method == 'POST':
        try:
            # Example: Create and save new product
            product_name = request.POST['name']
            product_price = float(request.POST['price'])
            product_size = request.POST['size']

            # Create a product instance
            product = Product(
                name=product_name,
                price=product_price,
                size=product_size
            )
            # Save the product to the database
            product.save()

            # Add another database operation (e.g., logging)
            # Some other model or operations that must also be saved atomically
            # Example: Log creation (optional)
            # Log.objects.create(action="Product created", product=product)

            return render(request, 'product_created.html', {'product': product})
        
        except Exception as e:
            # If any exception occurs, the transaction will be rolled back
            return render(request, 'error.html', {'error': str(e)})
    else:
        return render(request, 'create_product.html')
