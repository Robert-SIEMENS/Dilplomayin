from Controller import controller
from UI import ui
from GAN import gan

class Application:
    _instance = None
    m_controller = None
    m_ui = None
    m_gan = None
          
    @classmethod 
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = Application()
        return cls._instance
    
    def getUI(self):
        self.m_ui = ui.UI()
        return self.m_ui
    
    def getGAN(self):
        self.m_gan = gan.GAN()
        return self.m_gan
    
    def run(self):
        self.m_controller = controller.Controller()
        self.m_controller.run()