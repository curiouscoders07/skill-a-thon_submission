import csv
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data

        # Set the title and size of the main window
        self.setWindowTitle("Line Graph")
        self.setGeometry(100, 100, 800, 600)

        # Create a Matplotlib figure and add a subplot to it
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)

        # Set the x-axis and y-axis labels
        self.axes.set_xlabel("Subject")
        self.axes.set_ylabel("Goal Completion")

        # Plot the data as a line graph
        self.axes.plot(self.data)

        # Add the Matplotlib canvas to the PyQt5 window
        self.setCentralWidget(QWidget(self))
        self.layout = QVBoxLayout(self.centralWidget())
        self.layout.addWidget(self.canvas)

if __name__ == '__main__':
    exit=0
    f = open("mentee.txt", "r")
    sn = f.read()
    f.close()
    f1 = open("target.csv", "r")
    cr = csv.reader(f1)
    t = []
    if cr!=[]:
        exit=1
        for row in cr:
            if (row[0] == sn):
                l = [int(row[1]), int(row[2]), int(row[3]), int(row[4])]
                t.extend(l)
        f1.close()
        m = []
        f1 = open("tmarks.csv", "r")
        cr = csv.reader(f1)
        for row in cr:
            if (row[0] == sn):
                l = [int(row[1]), int(row[2]), int(row[3]), int(row[4])]
                m.extend(l)
        f1.close()
        data = []
        for i in range(4):
            p = (m[i] - t[i]) / t[i]
            data.append(p)
        # print(data)

        # Train a simple linear regression model on the data
        X = [[i] for i in range(len(data))]
        y = data
        model = LinearRegression()
        model.fit(X, y)

        # Use the trained model to make a prediction for the student's grade on the next assignment
        next_assignment_grade = model.predict([[len(data)]])

        # Create a PyQt5 application instance
        app = QApplication(sys.argv)

        # Create an instance of the MainWindow class and show it
        main_window = MainWindow(data)
        main_window.show()

            # Start the PyQt5 event loop
        sys.exit(app.exec_())
    if exit == 0:
        subprocess.call(['python', 'required.py'])
