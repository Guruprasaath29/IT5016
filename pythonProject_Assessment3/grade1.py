class GradingSystem:
    # Function to calculate the average score
    def average(self):
        # Prompt the user to input the number of subjects
        num = int(input("Enter the number of subjects:"))
        arr_scores = []
        # Input scores for each subject
        for i in range(num):
            input_score = int(input("Enter score:"))
            arr_scores.append(input_score)
        sum = 0
        # Calculate the sum of scores
        for i in arr_scores:
            sum = sum + i
        # Calculate the average score
        average = sum / len(arr_scores)
        # Print the average score
        print(average)
        # Return the average score
        return average
    
    # Function to assign grades based on the average score
    def grading(self):
        # Calculate the average score
        av = self.average()
        # Assign grades based on the average score
        if av > 90:
            print("First Class")
        elif av >= 70:
            print("Second Class Upper")
        elif av >= 60:
            print("Second Lower Class")
        elif av < 60 and av >= 50:
            print("Pass")
        elif av < 50:
            print("Fail")


# Comment explaining the use of the function
