<p align="center">
  <img src="https://github.com/Larabjorn/SDG-PROJECT-ACP/blob/main/ECO.png" width="350">
</p>

<h1 align = "center" tabindex="-1" class= "heading element" dir+"auto"> EcoDrive</h1>
<p align = " center" dir= "auto">
  <em>
    <code> Efficient Fuel Management Tool</code>
  </em>
</p>
<p align = "center" dir="auto">
  <b>IT-2104</b>
  <br>
  <a href="https://github.com/Larabjorn">
  LARA, BJORN PHILLIPE L.
  </a>
</p>
<hr></hr>
<h2> TABLE OF CONTENT</h2>
<ul dir="auto">
  <li>
    <a href="#-project-overview">Project Overview</a>
  </li>
  <li>
    <a href="#-PYTHON CONCEPTS AND LIBRARIES">PYTHON CONCEPTS AND LIBRARIES</a>
  </li>
  <li>
    <a href="#-CHOSEN SDG">CHOSEN SDG</a>
  </li>
  <li>
    <a href="#-INSTRUCTIONS ON HOW TO RUN THE PROGRAM">INSTRUCTIONS ON HOW TO RUN THE PROGRAM</a>
  </li>
   <li>
    <a href="#-Gratitude Statement">Gratitude Statement</a>
  </li>
</ul>
<hr></hr>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto"> PROJECT OVERVIEW</h2>
</div>
<p dir = "auto">
EcoDrive: Efficient Fuel Management Tool is a comprehensive Python-based application designed to help users monitor and analyze their fuel consumption efficiently. Developed using the Tkinter library, the application features an intuitive graphical user interface (GUI) that allows users to input and analyze their fuel data, compare fuel prices across gas stations, and visualize trends through interactive graphs.
</p>
<hr></hr>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">PYTHON CONCEPTS AND LIBRARIES
</div>
<ul dir="auto">
  <li>
    <h2>Object-Oriented Programming (OOP)</h2>
    <p>The application is built using a class, FuelTracker, which organizes code into reusable and modular components.</p>
    <h4>Encapsulation</h4>
    <p>Data (e.g., entries, station_data) and methods (e.g., add_entry, save_data) are encapsulated within the class.</p>
    <h3>Methods</h3>
    <p>Class methods are used to handle tasks, such as creating GUI components (create_add_entry_tab) or performing calculations (calculate_efficiency).</p>
</li>
  
  <li>
    <h2>Data Structures</h2>
    <h4>Lists</h4>
      <p>The entries list stores tuples containing data for each fuel entry (date, mileage, fuel, price, station).</p>
    <h4>Dictionaries</h4> 
      <p>A defaultdict is used to group fuel prices by gas station (station_data), enabling efficient storage and retrieval.</p>
</li>

  <li>
    <h2>File Handling</h2>
    <p>The save_data and load_data methods use JSON to save and load application data, making it persistent across sessions.</p>

</li>
  <li>
    <h2>Exception Handling</h2>
    <p>Input validation and error messages use try-except blocks to ensure user inputs are valid and prevent crashes.</p>
</li>
  <li>
    <h2>Datetime</h2>
    <p>The datetime module generates a list of the last 30 days for users to select a date easil
                (get_last_30_days).</p>

## Python Libraries
tkinter
        Used to create the graphical user interface (GUI). It manages components like labels, buttons, and dropdowns.
Widgets Used:
  ttk.Entry, ttk.Combobox, ttk.Button, and ttk.Checkbutton handle user input.
            
  ttk.Notebook organizes the interface into tabs (e.g., "Add Entry" and "Analysis").
            Grid Layout: Ensures the layout is responsive and centered.
Matplotlib
        This library is used to create graphs for visualizing fuel prices by station.
        Functions like plt.plot() and plt.show() generate line plots.
JSON
        The json module saves (dump) and loads (load) user data in a lightweight, portable format.
os
        Checks if the data file exists (os.path.exists) before loading data.

## GUI Features and Interactions
Dropdown Menus and Manual Entry
        Dropdowns (ttk.Combobox) provide pre-defined options for easier input (e.g., selecting mileage or fuel), while text entries allow flexibility for manual input.
Tab-Based Navigation
        The ttk.Notebook organizes the app into tabs for logical separation of features:
            Add Entry Tab: For entering fuel data.
            Analysis Tab: For toggling features, calculating efficiency, comparing stations, and viewing graphs.
 Buttons
        Buttons (ttk.Button) trigger specific functions, such as adding entries or calculating fuel efficiency.

Persistent Storage with JSON
    Save Functionality: The save_data method converts the entries list  and station_data dictionary into a JSON format and writes it to a file.

Load Functionality: The load_data method reads from the JSON file, ensuring all data is retained between sessions.

Core Functionalities and Their Python Implementation
    - Adding Entries
        User inputs (e.g., date, mileage, fuel) are validated and stored in the entries list.
        The station_data dictionary updates to include fuel prices grouped by station.
    - Fuel Efficiency Calculation
        Efficiency is calculated as total mileage / total fuel, and consumption as total fuel / total mileage. These calculations use basic Python arithmetic and list comprehensions.
    - Station Comparisons
        Average fuel prices for each station are computed using Python's sum() and len() functions, and the results are displayed in a messagebox.
    - Graphing
        The matplotlib.pyplot module is used to create line plots for station-wise fuel prices, making trends easy to understand.
Error Handling
    Validations prevent invalid inputs, such as empty fields or non-numeric values.
    Friendly error messages are shown via messagebox.showerror.
    
Flexibility and Extensibility
    Feature toggles (Checkbutton with BooleanVar) let users enable or disable analysis features, improving usability.
    New features (e.g., additional graph types or price trend predictions) can be added by expanding the class methods and tabs.
    
<p align="center">
  <img src="https://github.com/Larabjorn/SDG-PROJECT-ACP/blob/main/images.png">
</p>

## CHOSEN SDG
SDG 12: Responsible Consumption and Production
Sustainable Development Goals (SDG) Integration in the EcoDrive Project
The Fuel Tracker app not only helps users track fuel consumption but also aligns with several United Nations 

Reduces carbon emissions by fostering efficient fuel consumption.

By providing insights on fuel usage, the app encourages users to make more sustainable consumption choices, minimizing waste.


## INSTRUCTIONS ON HOW TO RUN THE PROGRAM
The guidelines below will help you understand how the EcoDrive: Efficient Fuel Management Tool works.

- Starting the Program
    Step 1: Run the program in a Python environment (e.g., IDLE, Jupyter Notebook, or any integrated IDE that supports Python).

    Step 2: Once the program starts, it will display a welcome message to greet the user.

    Step 3: The user will then be prompted to input their starting fuel level. The input should be in numerical format (e.g., liters of fuel). If the input is invalid (non-numeric), the program will ask for a valid input.

- Adding Fuel
    Step 4: After the initial fuel level is set, the program will allow the user to add fuel by entering the amount of fuel they added.

    Step 5: The program will update the total fuel count accordingly and provide a summary of the updated fuel status.

- Tracking Fuel Consumption
    Step 6: The program will prompt the user to input the amount of fuel consumed after each trip or refueling. The consumption input should be in liters.

    Step 7: After each entry, the program will update the fuel balance, showing the remaining fuel and how much was consumed.

    Step 8: If the fuel level becomes too low (e.g., below 5 liters), the program will alert the user to refuel.

- Viewing Fuel History
    Step 9: The program will also allow the user to view a history of their fuel transactions, including fuel added and fuel consumed.


    Step 10: The user can review the history at any time by selecting the "View History" option from the menu.


- Setting Fuel Alerts
    Step 11: Users can set alerts to notify them when their fuel reaches a specified level (e.g., 10 liters). The program will monitor the fuel level and send an alert when it’s time to refuel.


    Step 12: If the fuel level falls below the set alert threshold, the program will send a notification, reminding the user to refuel.


- Ending the Program
    Step 13: When the user decides to stop tracking, they can exit the program by selecting the "Exit" option from the main menu.

    Step 14: Upon exit, the program will save all data and display a thank you message, reminding the user to drive safely.


## Gratitude Statement
Completing this Fuel Tracker project has been a rewarding challenge. While coding is still an area I continue to learn and grow in, I am proud of the end result. I would like to express my heartfelt thanks to:

God for providing strength and wisdom to complete the project.
My family for their constant support and encouragement.
My professor for providing valuable insights and feedback throughout this journey.
Myself, for persevering through challenges and sticking with it.
This project aims to simplify fuel tracking and enhance the overall experience of users. I hope it serves its purpose and is a useful tool for all. Thank you for using the Fuel Tracker!

