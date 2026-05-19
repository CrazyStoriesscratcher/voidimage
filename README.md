img

A tiny Python library for drawing images on screen with simple commands.

Built on top of Pygame.

Installation:
    pip install img


    
Usage
    from img import Img


   i = Img()
   i.draw("image.png", 100, 150, 200) #(image_name,x,y,size_in_pixel)
   i.run()
