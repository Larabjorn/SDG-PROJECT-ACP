<p align="center">
  <img src="https://github.com/Larabjorn/SDG-PROJECT-ACP/blob/main/image%20project/ECO.png" width="350">
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
    <a href="#project-overview">I. Project Overview</a>
  </li>
  <li>
    <a href="#python-concepts-and-libraries">II. Python Concepts and Libraries</a>
  </li>
  <li>
    <a href="#chosen-sdg">III.Chosen SDG</a>
  </li>
  <li>
    <a href="#instructions-on-how-to-run-the-program">IV. Instructions on How to Run the Program</a>
  </li>
  <li>
    <a href="#gratitude-statement">V. Gratitude Statement</a>
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
    <img src="https://github.com/Larabjorn/SDG-PROJECT-ACP/blob/main/image%20project/images.png">
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
    <p>Step 2: Input the Customer Name in the designated field. This name will personalize the fuel entry records.</p>
      <p>Step 3: Input the starting fuel level (in liters) in numerical format. If invalid input is provided, the program will request a valid input.</p>
  </li>

  <li>
  <h3> Adding Fuel</h3>
      <p>Step 4: Add fuel by entering the amount added and other relevant details</p>
      <p> Step 5: The program updates the total fuel count and provides a summary.</p>
  </li>
  
  <li>
    <h3> Tracking Fuel Consumption</h3>
      <p>Step 6: Input the amount of fuel consumed after trips or refueling.</p>
      <p>Step 7: The program updates the fuel balance and alerts the user if fuel is too low.</p>
  </li>
  
  <li>
    <h3> Viewing Fuel History</h3>
      <p>Step 8: The program will also allow the user to view a history of their fuel transactions, including fuel added and fuel consumed.</p>
    <pre>
      <code>
         def create_view_history_tab(self):
        """Create the View History tab."""
        self.view_history_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_history_tab, text="View History")
        # Create Treeview for history
        columns = ("date", "mileage", "fuel", "price", "station")
        self.history_table = ttk.Treeview(
            self.view_history_tab, columns=columns, show="headings", height=20
        )
        self.history_table.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
      </code>
    </pre>
      <p>Step 9: The user can review the history at any time by selecting the "View History" option from the menu.</p>
  </li>
  <li>
    <h3> Ending the Program</h3>
      <p>Step 10: When the user decides to stop tracking, they can exit the program by selecting the "Exit" option from the main menu.</p>
  
  </li>
  </ul>

<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">Gratitude Statement</h2>
</div>
<ol dir = "auto">
  <ul dir="auto">
    <p>Completing this Fuel Tracker project has been a rewarding challenge. While coding is still an area I continue     to learn and grow in, I am proud of the end result. I would like to express my heartfelt thanks to:</p>
    <li>To our beloved Professor : Ma'am Fatima</li>
    <li>To my Mi Familia loved and support me</li>
    <li>To my mentor, bestu prendu, Jenrick Magtaas and friends</li>
    <li>Sa computer ko, hingalo na</li>
    <li>Sa pasensya ko, gabi gabi nalang pinapatayan ng wi-fi</li>
    <li>To myself that manage the struggles</li>
  </ul>


