import pytest
from imgoverlay.overlay import ImageOverlay

class TestImageOverlayStyle():

    def setup_class(self):
        '''
        This is run once when the test class is instantiated.
        '''
        print('Pytest running class setup routine...')

    def teardown_class(self):
        '''
        This is run once when all the tests in the class have been run.
        '''
        print('Pytest running class teardown routine...')

    def setup_method(self):
        '''
        This is run for each test method before the method runs.
        '''
        print('Pytest running method setup routine...')

    def teardown_method(self):
        '''
        This is run for each test method after the method completes.
        '''
        print('Pytest running method teardown routine...')
    
    def test_default_text_colour(self):
        '''
        Check that when we instantiate the image overlay class, the default
        text colour is set to 'black'.
        '''
        # Create an ImageOverlay instance
        overlay = ImageOverlay('test_image.jpg')
        # Check that the default colour is set to black
        assert overlay.text_colour == 'black'

    def test_set_valid_text_colour(self):
        '''
        Check that when we set a different (valid) text colour on an
        ImageOverlay class instance that this is stored.
        '''
        # Create an ImageOverlay instance and set the colour to white
        overlay = ImageOverlay('test_image.jpg')
        overlay.set_text_colour('white')
        # Check that the colour is now set to white
        assert overlay.text_colour == 'white'
    
    def test_set_invalid_text_colour(self):
        '''
        Check that when we set a different (invalid) text colour on an
        ImageOverlay class instance that a ValueError is raised.
        '''
        # Create an ImageOverlay instance
        overlay = ImageOverlay('test_image.jpg')
        # Check that a ValueError is raised when we set the colour to purple
        with pytest.raises(ValueError):
            overlay.set_text_colour('purple')

    def test_set_style_text_size(self):
        '''
        Check that when we use set_style to set a different text size that
        this is correctly stored.
        '''
        # Create an ImageOverlay instance
        overlay = ImageOverlay('test_image.jpg')
        # First verify that the default size is 72
        assert overlay.text_size == 72
        # Now set the font size to 36 and check this is stored.
        overlay.set_style(36, 'blue')
        assert overlay.text_size == 36
        
