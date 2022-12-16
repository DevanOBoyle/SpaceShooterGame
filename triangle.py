class Triangle:
    def __init__(self, coords):
        self.coords = coords
        self.x_coords = []
        self.y_coords = []
        for i in coords:
            self.x_coords.append(i[0])
            self.y_coords.append(i[1])

        self.x_shoot = self.x_coords[0]
        self.y_shoot = self.y_coords[0]

    def get_coords(self):
        return self.coords

    def collide_point(self, pos):
        if (pos[0] >= min(self.x_coords) and pos[0] <= max(self.x_coords)) and pos[1] >= min(self.y_coords) and pos[1] <= max(self.y_coords):
            return True
        return False

    def check_right_boundary(self, points):
        for i in self.x_coords:
            if i >= points[1][0]-1:
                return False
        return True

    def check_left_boundary(self, points):
        for i in self.x_coords:
            if i <= points[0][0]+1:
                return False
        return True

    def check_upper_boundary(self, points):
        for i in self.y_coords:
            if i <= points[0][1]+1:
                return False
        return True

    def check_lower_boundary(self, points):
        for i in self.y_coords:
            if i >= points[1][1]-1:
                return False
        return True

    def move_right(self, velocity):
        for i in range(3):
            self.coords[i][0] += velocity
            self.x_coords[i] = self.coords[i][0]
        self.x_shoot = self.x_coords[0]

    def move_left(self, velocity):
        for i in range(3):
            self.coords[i][0] -= velocity
            self.x_coords[i] = self.coords[i][0]
        self.x_shoot = self.x_coords[0]

    def move_up(self, velocity):
        for i in range(3):
            self.coords[i][1] -= velocity
            self.y_coords[i] = self.coords[i][1]
        self.y_shoot = self.y_coords[0]

    def move_down(self, velocity):
        for i in range(3):
            self.coords[i][1] += velocity
            self.y_coords[i] = self.coords[i][1]
        self.y_shoot = self.y_coords[0]

    def move_diamond(self, velocity, width, height, frame):
        if (max(self.x_coords) > width // 2 and min(self.y_coords) > (height// 5 - 50)):
            if self.check_upper_boundary(frame):
                self.move_up(velocity)
            if self.check_right_boundary(frame):
                self.move_right(velocity)
        elif (max(self.x_coords) > width // 2 and min(self.y_coords) <= (height// 5 - 50)):
            if self.check_upper_boundary(frame):
                self.move_up(velocity)
            if self.check_left_boundary(frame):
                self.move_left(velocity)
        elif (max(self.x_coords) <= width // 2 and min(self.y_coords) <= (height// 5 - 50)):
            if self.check_lower_boundary(frame):
                self.move_down(velocity)
            if self.check_left_boundary(frame):
                self.move_left(velocity)
        elif (max(self.x_coords) <= width // 2 and min(self.y_coords) > (height// 5 - 50)):
            if self.check_lower_boundary(frame):
                self.move_down(velocity)
            if self.check_right_boundary(frame):
                self.move_right(velocity)