from argparse import ArgumentParser
from imgoverlay.overlay import ImageOverlay


class OverlayApp:

    def __init__(self):
        print('Image Overlay Tool\n\n')
        self.parser = ArgumentParser(
            description='A simple tool for overlaying some text on an image.')
        self.parser.add_argument('image', type=str, nargs=1,
                                 help='The full path to the image file.')
        self.parser.add_argument('message', type=str, nargs=1,
                                 help='The message to overlay on the image.')
        self.parser.add_argument('-s', '--size', type=int,
                                 help='The font size of the text.')
        self.parser.add_argument('-c', '--colour', type=str,
                                 help='The colour of the text.')
        self.parser.add_argument(
            '-o', '--output', type=str,
            help='The name of the output file. If not specified, '
                 '"_overlay" is appended to the original file name.')

    def run(self):
        args = self.parser.parse_args()
        overlay = ImageOverlay(args.image)
        overlay.overlay_text(args.message)


if __name__ == '__main__':
    app = OverlayApp()
    app.run()
