from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking,Address

# Create your views here.
def create_booking(request):
	form=BookingForm
	if request.method == 'POST':
		bookForm=BookingForm(request.POST)
		print(request.POST)
		if bookForm.is_valid():
			bookForm.save()
			messages.success(request,'Data has been added')
			return redirect('/')
	return render(request,'add.html',{'form':form})






