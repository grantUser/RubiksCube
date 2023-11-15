class RubiksCube:
    """A class representing a Rubik's Cube."""

    def __init__(self):
        """Initialize a Rubik's Cube with default colors."""

        self.cube = {
            "U": [["W"] * 3 for _ in range(3)],
            "D": [["Y"] * 3 for _ in range(3)],
            "L": [["O"] * 3 for _ in range(3)],
            "R": [["R"] * 3 for _ in range(3)],
            "F": [["G"] * 3 for _ in range(3)],
            "B": [["B"] * 3 for _ in range(3)],
        }

    def display(self):
        """Display the current state of the Rubik's Cube."""

        for face in self.cube:
            print(face)
            for row in self.cube[face]:
                print(row)
            print()

    def is_complete(self):
        """Check if the Rubik's Cube is solved."""

        for face in self.cube:
            color = self.cube[face][0][0]
            for row in self.cube[face]:
                for sticker in row:
                    if sticker != color:
                        return False
        return True

    def rotate_face_clockwise(self, face):
        """Rotate a face of the Rubik's Cube clockwise."""

        self.cube[face] = list(zip(*reversed(self.cube[face])))

    def rotate_face_counter_clockwise(self, face):
        """Rotate a face of the Rubik's Cube counter-clockwise."""

        self.cube[face] = list(reversed(list(zip(*self.cube[face]))))

    def move_U(self):
        """Perform the U (up) move on the Rubik's Cube."""

        self.rotate_face_clockwise("U")
        temp_row = list(self.cube["F"][0])
        self.cube["F"][0] = self.cube["R"][0]
        self.cube["R"][0] = self.cube["B"][0]
        self.cube["B"][0] = self.cube["L"][0]
        self.cube["L"][0] = temp_row

    def move_U_prime(self):
        """Perform the U' (up prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("U")
        temp_row = list(self.cube["F"][0])
        self.cube["F"][0] = self.cube["L"][0]
        self.cube["L"][0] = self.cube["B"][0]
        self.cube["B"][0] = self.cube["R"][0]
        self.cube["R"][0] = temp_row

    def move_R(self):
        """Perform the R (right) move on the Rubik's Cube."""

        self.rotate_face_clockwise("R")
        for i in range(3):
            temp = self.cube["U"][i][2]
            self.cube["U"][i][2] = self.cube["F"][i][2]
            self.cube["F"][i][2] = self.cube["D"][i][2]
            self.cube["D"][i][2] = self.cube["B"][2 - i][0]
            self.cube["B"][2 - i][0] = temp

    def move_R_prime(self):
        """Perform the R' (right prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("R")
        for i in range(3):
            temp = self.cube["U"][i][2]
            self.cube["U"][i][2] = self.cube["B"][2 - i][0]
            self.cube["B"][2 - i][0] = self.cube["D"][i][2]
            self.cube["D"][i][2] = self.cube["F"][i][2]
            self.cube["F"][i][2] = temp

    def move_L(self):
        """Perform the L (left) move on the Rubik's Cube."""

        self.rotate_face_clockwise("L")
        for i in range(3):
            temp = self.cube["U"][i][0]
            self.cube["U"][i][0] = self.cube["B"][2 - i][2]
            self.cube["B"][2 - i][2] = self.cube["D"][i][0]
            self.cube["D"][i][0] = self.cube["F"][i][0]
            self.cube["F"][i][0] = temp

    def move_L_prime(self):
        """Perform the L' (left prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("L")
        for i in range(3):
            temp = self.cube["U"][i][0]
            self.cube["U"][i][0] = self.cube["F"][i][0]
            self.cube["F"][i][0] = self.cube["D"][i][0]
            self.cube["D"][i][0] = self.cube["B"][2 - i][2]
            self.cube["B"][2 - i][2] = temp

    def move_D(self):
        """Perform the D (down) move on the Rubik's Cube."""

        self.rotate_face_clockwise("D")
        temp_row = list(self.cube["F"][2])
        self.cube["F"][2] = self.cube["L"][2]
        self.cube["L"][2] = self.cube["B"][2]
        self.cube["B"][2] = self.cube["R"][2]
        self.cube["R"][2] = temp_row

    def move_D_prime(self):
        """Perform the D' (down prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("D")
        temp_row = list(self.cube["F"][2])
        self.cube["F"][2] = self.cube["R"][2]
        self.cube["R"][2] = self.cube["B"][2]
        self.cube["B"][2] = self.cube["L"][2]
        self.cube["L"][2] = temp_row

    def move_F(self):
        """Perform the F (front) move on the Rubik's Cube."""

        self.rotate_face_clockwise("F")
        for i in range(3):
            temp = self.cube["U"][2][i]
            self.cube["U"][2][i] = self.cube["L"][2 - i][2]
            self.cube["L"][2 - i][2] = self.cube["D"][0][2 - i]
            self.cube["D"][0][2 - i] = self.cube["R"][i][0]
            self.cube["R"][i][0] = temp

    def move_F_prime(self):
        """Perform the F' (front prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("F")
        for i in range(3):
            temp = self.cube["U"][2][i]
            self.cube["U"][2][i] = self.cube["R"][i][0]
            self.cube["R"][i][0] = self.cube["D"][0][2 - i]
            self.cube["D"][0][2 - i] = self.cube["L"][2 - i][2]
            self.cube["L"][2 - i][2] = temp

    def move_B(self):
        """Perform the B (back) move on the Rubik's Cube."""

        self.rotate_face_clockwise("B")
        for i in range(3):
            temp = self.cube["U"][0][i]
            self.cube["U"][0][i] = self.cube["R"][2 - i][2]
            self.cube["R"][2 - i][2] = self.cube["D"][2][2 - i]
            self.cube["D"][2][2 - i] = self.cube["L"][i][0]
            self.cube["L"][i][0] = temp

    def move_B_prime(self):
        """Perform the B' (back prime) move on the Rubik's Cube."""

        self.rotate_face_counter_clockwise("B")
        for i in range(3):
            temp = self.cube["U"][0][i]
            self.cube["U"][0][i] = self.cube["L"][i][0]
            self.cube["L"][i][0] = self.cube["D"][2][2 - i]
            self.cube["D"][2][2 - i] = self.cube["R"][2 - i][2]
            self.cube["R"][2 - i][2] = temp
