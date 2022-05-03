from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking,Address

# Create your views here.
def home(request):
	form=BookingForm
	print("444444444444444444444")
	if request.method == 'POST':
		bookForm=BookingForm(request.POST)
		print(request.POST)
		print("777777777777777777")
		if bookForm.is_valid():
			print("00000")
			#bookForm.user = request.user
			bookForm.save()
			messages.success(request,'Data has been added')
			return redirect('/')
	return render(request,'index.html',{'form':form})





# def home(request):
# 	form=BookingForm

# 	if request.method =='POST':
# 		form =BookingForm(request.POST)
# 		if form.is_valid():
# 		     form.save()
# 	context = {'form':form}
# 	return render(request,'index.html',context)