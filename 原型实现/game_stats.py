class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.page = 'Start'
        self.username_input = False
        self.password_input = False
        self.user_info = {}
        self.game_record = {}
        self.player = ''
        self.count = 0
        self.step = 0
        self.time = 0
        self.game_active = True
        self.game_set = False
