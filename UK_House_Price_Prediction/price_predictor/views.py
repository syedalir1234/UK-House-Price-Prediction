from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .prediction import predict_property
# Create your views here.


def index(request):
    return render(request, 'front_page.html')


class PredictPropertyView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Extract parameters from the request
            features = {
                'lotdepth': float(request.GET.get('lotdepth')),
                'community': request.GET.get('community'),
                'washrooms': int(request.GET.get('washrooms')),
                'brokerage': request.GET.get('brokerage'),
                'sqft': float(request.GET.get('sqft')),
                'lotfront': float(request.GET.get('lotfront')),
                'type': request.GET.get('type'),
                'kitchens_plus': int(request.GET.get('kitchens_plus')),
                'style': request.GET.get('style'),
                'rooms_plus': int(request.GET.get('rooms_plus')),
                'rooms': int(request.GET.get('rooms')),
                'garage_spaces': int(request.GET.get('garage_spaces')),
                'parking_spaces': int(request.GET.get('parking_spaces')),
            }

            # Call the predict_property function
            predicted_price = predict_property(
                features,
            )

            # Return the predicted price as a JSON response
            return JsonResponse({'predicted_price': round(int(predicted_price), 2)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)