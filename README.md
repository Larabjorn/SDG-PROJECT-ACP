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
<h2>Table of Contents</h2>
<ul>
  <li>
    <a href="#project-overview">Project Overview</a>
  </li>
  <li>
    <a href="#python-concepts-and-libraries">Python Concepts and Libraries</a>
  </li>
  <li>
    <a href="#chosen-sdg">Chosen SDG</a>
  </li>
  <li>
    <a href="#instructions-on-how-to-run-the-program">Instructions on How to Run the Program</a>
  </li>
  <li>
    <a href="#gratitude-statement">Gratitude Statement</a>
  </li>
</ul>
<hr>


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
    <p>The application is built using a class, <code>FuelTracker</code>, which organizes code into reusable and modular components.</p>
    <h4>Encapsulation</h4>
    <p>Data (e.g., <code>entries</code>, <code>station_data</code>) and methods (e.g., <code>add_entry</code>, <code>save_data</code>) are encapsulated within the class.</p>
    <h4>Methods</h4>
    <p>Class methods are used to handle tasks, such as creating GUI components (<code>create_add_entry_tab</code>) or performing calculations (<code>calculate_efficiency</code>).</p>
</li>
  
  <li>
    <h2>Data Structures</h2>
    <h4>Lists</h4>
      <p>The <code>entries</code> list stores tuples containing data for each fuel entry (date, mileage, fuel, price, station).</p>
    <h4>Dictionaries</h4> 
      <p>A <code>defaultdict</code> is used to group fuel prices by gas station (<code>station_data</code>), enabling efficient storage and retrieval.</p>
</li>

  <li>
    <h2>File Handling</h2>
    <p>The <code>save_data</code> and <code>load_data</code> methods use JSON to save and load application data, making it persistent across sessions.</p>

</li>
  <li>
    <h2>Exception Handling</h2>
    <p>Input validation and error messages use <code>try-except</code> blocks to ensure user inputs are valid and prevent crashes.</p>
</li>
  <li>
    <h2>Datetime</h2>
    <p>The <code>datetime</code> module generates a list of the last 30 days for users to select a date easil
                (<code>get_last_30_days</code>).</p>
</li>
</ul>
  
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Python Libraries
</div>
<ul dir="auto">
<li>
    <h2>tkinter</h2>
    <p>Used to create the graphical user interface (GUI). It manages components like labels, buttons, and dropdowns.
</p>
</li>
  <h3>Widgets Used:</h3>
        <p><code>ttk.Entry</code>, <code>ttk.Combobox</code>, <code>ttk.Button</code>, and <code>ttk.Checkbutton</code> handle user input.</p>
        <p><code>ttk.Notebook</code> organizes the interface into tabs (e.g., "Add Entry" and "Analysis").</p>
        <p>Grid Layout: Ensures the layout is responsive and centered.</p>
</li>
  
<li>
  <h2>Matplotlib</h2>
        <p>This library is used to create graphs for visualizing fuel prices by station.</p>
        <p>Functions like <code>plt.plot()</code> and <code>plt.show()</code> generate line plots.</p>
</li>
  
<li>
  <h2>JSON</h2>
        <p>The <code>json</code> module saves (<code>dump</code>) and loads (load) user data in a lightweight, portable format.</p>
</li>
  
<li>
  <h2>os</h2>
        <p>Checks if the data file exists (<code>os.path.exists</code>) before loading data.</p>
</li>
</ul>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">GUI Features and Interactions
</div>
<ul dir="auto">
<li>    
  <h2>Dropdown Menus and Manual Entry</h2>
        <p>Dropdowns (<code>ttk.Combobox</code>) provide pre-defined options for easier input (e.g., selecting mileage or fuel), while text entries allow flexibility for manual input.</p>
</li>
<li>
  <h2>Tab-Based Navigation</h2>
        <p>The <code>ttk.Notebook organizes</code> the app into tabs for logical separation of features:
            <h4>Add Entry Tab</h4> <p>For entering fuel data.</p>
            <h4>Analysis Tab</h4> <p>For toggling features, calculating efficiency, comparing stations, and viewing graphs.</p>
</li>
 <h2>Buttons</h2>
        <p>Buttons (<code>ttk.Button</code>) trigger specific functions, such as adding entries or calculating fuel efficiency.</p>
</li>
</ul>
    
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Persistent Storage with JSON
</div>
<ul dir="auto">
<li>
    <h2>Save Functionality</h2> 
        <p>The <code>save_data</code> method converts the <code>entries</code> list and <code>station_data</code> dictionary into a JSON format and writes it to a file.</p>
</li>
<li>
    <h2>Load Functionality</h2> 
  <p>The <code>load_data</code> method reads from the JSON file, ensuring all data is retained between sessions.</p>
</li>
</ul>
    
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Core Functionalities and Their Python Implementation
</div>
<ul dir="auto">
<li>
    <h2>Adding Entries</h2>
        <p>User inputs (e.g., date, mileage, fuel) are validated and stored in the <code>entries</code> list.</p>
        <p>The <code>station_data</code> dictionary updates to include fuel prices grouped by station.</p>
</li>
<li>
    <h2>Fuel Efficiency Calculation</h2>
        <p>Efficiency is calculated as total mileage / total fuel, and consumption as total fuel / total mileage. These calculations use basic Python arithmetic and list comprehensions.</p>
</li> 
<li>
    <h2>Station Comparisons</h2>
        <p>Average fuel prices for each station are computed using Python's <code>sum()</code> and <code>len()</code> functions, and the results are displayed in a <code>messagebox</code>.</p>
</li>
<li>
    <h2>Graphing</h2>
        <p>The <code>matplotlib.pyplot</code> module is used to create line plots for station-wise fuel prices, making trends easy to understand.</p>
</li>
</ul>
    
  <div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Error Handling
</div>
<ul dir="auto">
<li>
    <p>Validations prevent invalid inputs, such as empty fields or non-numeric values.</p>
    <p>Friendly error messages are shown via <code>messagebox.showerror</code>.</p>
</li>
</ul>
  <div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Flexibility and Extensibility
</div>
<ul dir="auto">
<li>
    <p>Feature toggles (<code>Checkbutton</code> with <code>BooleanVar</code>) let users enable or disable analysis features, improving usability.</p>
    <p>New features (e.g., additional graph types or price trend predictions) can be added by expanding the class methods and tabs.</p>
</li>
</ul>

<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">CHOSEN SDG</h2>
</div>
<p dir = "auto">
    <h3>SDG 12: Responsible Consumption and Production</h3>
    <img src="https://github.com/Larabjorn/SDG-PROJECT-ACP/blob/main/images.png">
    Sustainable Development Goals (SDG) Integration in the EcoDrive Project
    The Fuel Tracker app not only helps users track fuel consumption but also aligns with several United Nations 
<br>
  <br>
    Reduces carbon emissions by fostering efficient fuel consumption.
<br>
  <br>
    By providing insights on fuel usage, the app encourages users to make more sustainable consumption choices,          minimizing waste.
</p>
<hr></hr>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">INSTRUCTIONS ON HOW TO RUN THE PROGRAM</h2>
</div>
<ol dir = "auto">
  <ul dir="auto">
    <h4>The guidelines below will help you understand how the EcoDrive: Efficient Fuel Management Tool works.</h4>
  <li>
    <h3> Starting the Program</h3>
      <p>Step 1: Run the program in a Python environment (e.g., IDLE, Jupyter Notebook, or any integrated IDE that supports Python).</p>
      <p>Step 2: The user will then be prompted to input their starting fuel level. The input should be in numerical format (e.g., liters of fuel). If the input is invalid (non-numeric), the program will ask for a valid input.</p>
  </li>

  <li>
  <h3> Adding Fuel</h3>
      <p>Step 3: After the initial fuel level is set, the program will allow the user to add fuel by entering the amount of fuel they added.</p>
      <p> Step 4: The program will update the total fuel count accordingly and provide a summary of the updated fuel status.</p>
  </li>
  
  <li>
    <h3> Tracking Fuel Consumption</h3>
      <p>Step 5: The program will prompt the user to input the amount of fuel consumed after each trip or refueling. The consumption input should be in liters.</p>
      <p>Step 6: After each entry, the program will update the fuel balance, showing the remaining fuel and how much was consumed.</p>
      <p>Step 7: If the fuel level becomes too low (e.g., below 5 liters), the program will alert the user to refuel.</p>
  </li>
  
  <li>
    <h3> Viewing Fuel History</h3>
      <p>Step 8: The program will also allow the user to view a history of their fuel transactions, including fuel added and fuel consumed.</p>
    <pre>
      <code>
        def save_data(self):
          """Save entries and station data to a JSON file."""
          with open("fuel_data.json", "w") as f:
              json.dump({"entries": self.entries, "station_data": self.station_data}, f)
      </code>
    </pre>
      <p>Step 9: The user can review the history at any time by selecting the "View History" option from the menu.</p>
    <pre>
      <code>
        {"entries": [
        ["2024-11-24", 50.0, 5.0, 320.0, "Petron"], 
        ["2024-11-25", 60.0, 3.0, 200.0, "Seaoil"], 
        ["2024-11-24", 60.0, 9.0, 1000.0, "Phoenix"],
        ...
        "station_data": 
        {"Petron": [320.0, 640.0, 1450.0, 456.0, 2.0, 1.5, 2.25, 1.75], 
        "Seaoil": [200.0, 623.0], 
        "Phoenix": [1000.0, 563.0], 
        "Shell": [200.0, 755.0, 73.0, 453.0, 565.0, 2.5, 1.5, 1.75, 2.5, 1.5, 1.5, 1.5, 1.5], 
        "Petro Gazz": [546.0]}}
      </code>
    </pre>
  </li>

  <li>
  <h3> Setting Fuel Alerts</h3>
      <p>Step 10: Users can set alerts to notify them when their fuel reaches a specified level (e.g., 10 liters). The program will monitor the fuel level and send an alert when it’s time to refuel.</p>
      <p>Step 11: If the fuel level falls below the set alert threshold, the program will send a notification, reminding the user to refuel.</p>
  </li>

  <li>
    <h3> Ending the Program</h3>
      <p>Step 12: When the user decides to stop tracking, they can exit the program by selecting the "Exit" option from the main menu.</p>
      <p>Step 13: Upon exit, the program will save all data and display a thank you message, reminding the user to drive safely.</p>
  </li>
  </ul>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Gratitude Statement</h2>
</div>
<ol dir = "auto">
  <ul dir="auto">
    <p>Completing this Fuel Tracker project has been a rewarding challenge. While coding is still an area I continue     to learn and grow in, I am proud of the end result. I would like to express my heartfelt thanks to:</p>
    <li>To our beloved SANRIO Fan din : Ma'am Fatima</li>
    <li>To my Mi Familia loved and support me</li>
    <li>To my mentor, bestu prendu, Jenrick Magtaas and friends</li>
    <li>Sa computer ko, hingalo na</li>
    <li>Sa pasensya ko, gabi gabi nalang pinapatayan ng wi-fi</li>
    <li>To myself that manage the struggles, still look good and have nice fits</li>
  </ul>


