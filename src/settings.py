class Settings():
    """存储`外星人入侵`的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 移动速度设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 7

        # 外星人设置
        self.alien_speed_factor = 1
        # 外星人撞到屏幕边缘后下移的速度
        self.fleet_drop_speed = 10
        # fleet_directiron = 1表示右移，-1表示左移
        self.fleet_direction = 1
