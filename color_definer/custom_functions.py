from PIL import Image


def get_image_color(filename):
    image = Image.open(filename)
    image_rgb = image.convert('RGB')
    rgb = image_rgb.getcolors(maxcolors=256000)[0][1]
    return '#%02x%02x%02x' % rgb

    '''
    print('#{:02x}{:02x}{:02x}'.format(rgb[0],rgb[1],rgb[2]))
    '''
