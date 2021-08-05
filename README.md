## Skin-Type-Prediction Website using Flask

This Project is influenced by [Abhishek Thakur](https://www.youtube.com/watch?v=BUh76-xD5qU)  
I already made and save model.pth using [link](https://github.com/JustCal1MeLee/cnn_skin-classfication_makemodel_practice)  
That model doesn't work well because I have a little data.   


Before prediction
<center> <img src="/img/webpage1.png" width="300" height="300"> </center>

<center>
After prediction
<img src="/img/webpage3.png" width="300" height="300">
</center>

### Tech/framework used 
* Python 3
  - Flask==2.0.1
  - torch==1.9.0+cpu (pytorch)
  - torchvision==0.10.0+cpu
  - Pillow==8.2.0
* HTML
* CSS
  - Using Bootstrap library and example

### Motivation
My team is participated in K-iCorps Program which help college student's startup.  
And I'm trying to make application about skin-type prediction and recommend cosmetics based on that prediction.  
This is the first time that I learn Flask. so if you have a feedback, please tell me.

### Description
Using model.pth nad pytorch, we can load the image classfication model.  
When we upload image, we can save image into "/static"  
And transform the image, that function is simillar to code that I made model before.    
After finishing image transformation, we can input image into that model, and find estimated value.  
And that value and image that you uploaded will be showed in webpage

### How to use
You can change 2 parts
1. Insert your model.pth
2. Change labels 
Plus, if you don't like webpage style, you can also change it.  

### License
MIT © JustCal1MeLee
