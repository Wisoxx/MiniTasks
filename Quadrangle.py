import math


"""
Write a class "Quadrangle". Attributes are 4 points each of which is presented as a tuple with 2 numbers (x, y).
Method info() returns information about coordinates of each point.
Method get_type() calculates if the figure is a rectangle, square, parallelogram, trapezoid or rhombus.
If the figure isn't any of mentioned, a special message is returned.
Method get_area() calculates and returns the area 
"""


class Quadrangle:
    """
                                                                                            B
    B-----------------C     B-------C          B----------C         B----------C           / \
    |                 |     |       |         /          /         /|           \       A /   \ C
    |                 |     |       |        /          /         / |            \        \   /
    A-----------------D     A-------D       A----------D         A--K-------------D        \ /
                                                                                            D
    """
    def __init__(self, A: tuple[float, float], B: tuple[float, float], C: tuple[float, float], D: tuple[float, float]):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.type = None
        self.area = None

    def info(self):
        return {"A": self.A, "B": self.B, "C": self.C, "D": self.D}

    @staticmethod
    def points_distance(A: tuple[float, float], B: tuple[float, float]):
        return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)  # i.e. sqrt( (x2-x1)^2 + (y2-y1)^2 )

    def lines_distance(self, line1: tuple[tuple[float, float], tuple[float, float]],
                             line2: tuple[tuple[float, float], tuple[float, float]]):
        """
        Attention: returns incorrect results if used when a perpendicular line isn't the shortest way
        """
        if not self.is_parallel(line1, line2):
            print("Error: lines aren't parallel")
            return -1

        a1, b1 = self.get_line_equation(*line1)
        b2 = self.get_line_equation(*line2)[1]

        # finding the distance between the lines from their equations
        distance = abs(b2-b1)/math.sqrt(1+a1**2)
        return distance

    @staticmethod
    def get_vector(A: tuple[float, float], B: tuple[float, float]):
        return B[0] - A[0], B[1] - A[1]

    @staticmethod
    def get_line_equation(A: tuple[float, float], B: tuple[float, float]):
        # y = ax + b
        a = (B[1]-A[1])/(B[0]-A[0])  # a = (y2 - y1)/(x2 - x1)
        b = B[1] - a * B[0]  # b = y - a * x
        return a, b

    def is_parallel(self, line1: tuple[tuple[float, float], tuple[float, float]],
                          line2: tuple[tuple[float, float], tuple[float, float]]):
        if self.get_line_equation(*line1)[0] == self.get_line_equation(*line2)[0]:  # if coefficients 'a' are equal
            return True
        return False

    def get_angle(self, line1: tuple[tuple[float, float], tuple[float, float]],
                        line2: tuple[tuple[float, float], tuple[float, float]]):
        len1 = self.points_distance(line1[0], line1[1])
        len2 = self.points_distance(line2[0], line2[1])
        if len1 == 0 or len2 == 0:
            return 0
        line1 = self.get_vector(line1[0], line1[1])
        line2 = self.get_vector(line2[0], line2[1])
        return math.acos((line1[0]*line2[0] + line1[1]*line2[1])/(len1 * len2))  # i.e. arccos((x1*x2 + y1*y2)/(len1*len2))

    def get_type(self):  # TODO create an exception for 0 length
        if not self.type:
            AB = self.points_distance(self.A, self.B)
            BC = self.points_distance(self.B, self.C)
            CD = self.points_distance(self.C, self.D)
            AD = self.points_distance(self.A, self.D)
            ang_A = self.get_angle((self.A, self.D), (self.A, self.B))
            ang_B = self.get_angle((self.B, self.C), (self.A, self.B))
            ang_C = self.get_angle((self.B, self.C), (self.C, self.D))
            ang_D = self.get_angle((self.A, self.D), (self.D, self.C))
            print(ang_A, ang_B, ang_C, ang_D)
            AB_parallel_CD = self.is_parallel((self.A, self.B), (self.C, self.D))
            BC_parallel_AD = self.is_parallel((self.B, self.C), (self.A, self.D))
            match AB_parallel_CD, BC_parallel_AD:
                case True, True:
                    pass
                case _:
                    pass
            pass  # TODO
        # TODO make the program rearrange the points when needed
        return self.type

    def get_area(self):
        if self.area:
            return self.area

        AB = self.points_distance(self.A, self.B)
        BC = self.points_distance(self.B, self.C)
        match self.type:
            case "rectangle":
                # area = length * width
                self.area = AB * BC

            case "square":
                # area = side^2
                self.area = AB**2

            case "parallelogram":
                # area = height * base
                height = self.lines_distance((self.A, self.D), (self.B, self.C))
                self.area = BC * height  # because BC = AD

            case "trapezoid":
                # TODO move the if to get_type()
                if not self.is_parallel((self.A, self.D), (self.B, self.C)):
                    self.A, self.B, self.C, self.D = self.B, self.C, self.D, self.A  # rotating it 90° if DA and BC aren't bases
                    BC = self.points_distance(self.B, self.C)
                # area = height * (base1 + base2)/2
                DA = self.points_distance(self.D, self.A)

                height = self.lines_distance((self.A, self.D), (self.B, self.C))
                self.area = height * (DA + BC)/2

            case "rhombus":
                diagonal1 = self.points_distance(self.A, self.C)
                diagonal2 = self.points_distance(self.B, self.D)
                self.area = diagonal1 * diagonal2 / 2

            case _:
                print("Class Quadrangle doesn't support calculating the area of this figure.")
                return -1

        return self.area


if __name__ == "__main__":
    abc = Quadrangle((0, 0), (0, 3), (5, 3), (5, 0))
    # abc.type = "rectangle"
    print(abc.get_type())
