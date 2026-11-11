def calculate_average(values):
   if not values:
       raise ValueError("Values cannot be empty")

   return sum(values) / len(values)

def summarize_project():
	return "Git Tutorials : to learn git and learning python developement workflow"
