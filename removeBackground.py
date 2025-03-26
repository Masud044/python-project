import easygui
from rembg import remove
from PIL import Image
import io


input_path = easygui.fileopenbox(title="Select an Image to Remove Background", filetypes=["*.jpg", "*.png"])


if input_path:
    try:
        
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()

        
        output_data = remove(input_data)

        
        output_path = easygui.filesavebox(title="Save Output Image", default="nature1.jpeg", filetypes=["*.jpeg"])

        if output_path:
            
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)

            
            output_image = Image.open(io.BytesIO(output_data))
            output_image.show()

            easygui.msgbox(f"Background removed successfully! Output saved as {output_path}", title="Success")

        else:
            easygui.msgbox("No output path selected. Exiting.", title="Error")

    except Exception as e:
        easygui.msgbox(f"An error occurred: {e}", title="Error")
