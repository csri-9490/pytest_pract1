
class Screenshots:
    def __init__(self,driver):
        self.driver=driver

    def getscreenshots(self,filename):
        return self.dirver.save_screenshot(filename)
