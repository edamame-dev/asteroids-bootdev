import pygame

class TriangleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, size, rotation=0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size
        self.rotation = rotation

    def calculate_vertices(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.size / 1.5

        a = self.position + forward * self.size
        b = self.position - forward * self.size - right
        c = self.position - forward * self.size + right

        return [a, b, c]

    def draw(self, screen):

            pygame.draw.polygon(screen, "blue", self.calculate_vertices(), 1)

            vertices = self.calculate_vertices()
            for vertex in vertices:
                pygame.draw.circle(screen, "red", vertex, 5)  # Small circles at each vertex

    def update(self, dt):

        pass

    def check_collision(self, circle):
        vertices = self.calculate_vertices()

        for vertex in vertices:
            if vertex.distance_to(circle.position) <= circle.radius:
                return True

        for i in range(len(vertices)):
            start_point = vertices[i]
            end_point = vertices[(i + 1) % len(vertices)]  
            if self.line_collision(start_point, end_point, circle.position, circle.radius):
                return True

        if self.point_in_triangle(circle.position, vertices):
            return True

        return False

    @staticmethod
    def line_collision(start, end, circle_center, circle_radius):
        segment = end - start
        to_circle_center = circle_center - start

        segment_length = segment.length()
        segment_dir = segment.normalize()
        projection_length = to_circle_center.dot(segment_dir)
        projection_point = start + segment_dir * max(0, min(projection_length, segment_length))

        return projection_point.distance_to(circle_center) <= circle_radius

    @staticmethod
    def point_in_triangle(point, vertices):
        a, b, c = vertices
        cross1 = (b - a).cross(point - a)
        cross2 = (c - b).cross(point - b)
        cross3 = (a - c).cross(point - c)

        return (cross1 >= 0 and cross2 >= 0 and cross3 >= 0) or (cross1 <= 0 and cross2 <= 0 and cross3 <= 0)
