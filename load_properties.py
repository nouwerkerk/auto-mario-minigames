class Properties(object):
    def __init__(self):
        self.topScreenBounds = [0, 0, 1920, 1080]
        self.bottomScreenBounds = [0, 0, 1920, 1080]
        self.scale = 1.0
        self.dimensions = [1920, 1080]

    def loadFile(self, path):
        with open(path, 'r') as f:
            for line in f.readlines():
                #Don't read comments
                if line.startswith("#"):
                    continue

                #Scale
                if "Scale" in line:
                    self.scale = float(line.split("=",1)[1])

                #Top screen
                if "top" in line:
                    if "ScreenX" in line:
                        self.topScreenBounds[0] = int(line.split("=",1)[1])
                    if "ScreenY" in line:
                        self.topScreenBounds[1] = int(line.split("=",1)[1])

                #Bottom screen
                elif "bottom" in line:
                    if "ScreenX" in line:
                        self.bottomScreenBounds[0] = int(line.split("=",1)[1])
                    if "ScreenY" in line:
                        self.bottomScreenBounds[1] = int(line.split("=",1)[1])

                #Screen dimensions
                elif "screenWidth" in line:
                    self.topScreenBounds[2] = int(line.split("=", 1)[1])
                    self.bottomScreenBounds[2] = int(line.split("=", 1)[1])
                elif "screenHeight" in line:
                    self.topScreenBounds[3] = int(line.split("=", 1)[1])
                    self.bottomScreenBounds[3] = int(line.split("=", 1)[1])

        f.close()

properties = Properties()