# This file consists of Test Information like username, password, XPATH, etc.

# Python Class for Login
class OrangeHRM_Login:
    # Login Details
    username = "Admin"
    password = "admin123"
    # Selenium selector for Login Details
    username_NAME = "username"
    password_NAME = "password"
    login_XPATH = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
class OrangeHRM_Search:
    # Search Input in LowerCase
    admin = "admin"
    pim = "pim"
    leave = "leave"
    time = "time"
    recruitment = "recruitment"
    my_info = "my info"
    performance = "performance"
    dashboard = "dashboard"
    directory = "directory"
    maintenance = "maintenance"
    buzz = "buzz"
    # Search Input in UpperCase
    ADMIN = "ADMIN"
    PIM = "PIM"
    LEAVE = "LEAVE"
    TIME = "TIME"
    RECRUITMENT = "RECRUITMENT"
    MY_INFO = "MY INFO"
    PERFORMANCE = "PERFORMANCE"
    DASHBOARD = "DASHBOARD"
    DIRECTORY = "DIRECTORY"
    MAINTENANCE = "MAINTENANCE"
    BUZZ = "BUZZ"
    # Selenium Selectors for Search
    search = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    Admin_NAME = "Admin"
    PIM_NAME = "PIM"
    Leave_NAME = "Leave"
    Time_NAME = "Time"
    Recruitment_NAME = "Recruitment"
    My_Info_NAME = "My Info"
    Performance_NAME = "Performance"
    Dashboard_NAME = "Dashboard"
    Directory_NAME = "Directory"
    Maintenance_NAME = "Maintenance"
    cancel = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[1]'
    Buzz_NAME = "Buzz"
    
class OrangeHRM_Admin:
    # Selenium Selectors for User Admin
    user_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    users = "Users"
    user_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    user_role_admin = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    user_role_ESS = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/span'
    admin_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    admin_status_Enabled = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span'
    admin_status_Disabled ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]/span'
    search = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    
class OrangeHRM_Add:
    # New Employee Details
    firstname= "Desabandhu"
    middlename ="R"
    lastname = "S"
    PIM_username = "Desabandhu R S"
    PIM_password = 'HelloWorld65$'
    # Selenium selectors for New Employee
    add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    firstname_NAME = "firstName"
    middlename_NAME = "middleName"
    lastname_NAME = "lastName"
    create_login_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    PIM_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label'
    PIM_username_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    PIM_password_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    PIM_confirm_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    PIM_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'


class OrangeHRM_Edit:
    # Selenium Selectors for Editing Emplyee Details
    employee_NAME = "//div[text()='Desabandhu R']//parent::div"
    Personal_Details = "Personal Details"
    Contact_Details = "Contact Details"
    Emergency_Contacts = "Emergency Contacts"
    Dependents = "Dependents"
    Immigration = "Immigration"
    Job = "Job"
    Salary = "Salary"
    Tax_Exemptions = "Tax Exemptions"
    Report_to = "Report-to"
    Qualifications = "Qualifications"
    Memberships = "Memberships"
    
class OrangeHRM_Personal_Details:
    # Employee Details
    Nickname = "Buvanesh"
    Other_ID = "AT10"
    Driver_License_Number = "TN10AD2982520"
    License_Expiry_Date = "2027-07-01"
    SSN_Number = "5165165464"
    SIN_Number = "32115451205"
    DOB = "2000-02-04"
    Military = "No"
    # Selenium Selectors for Personal_Details
    Nickname_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    Other_ID_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    Driver_License_Number_XPATH= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    License_Expiry_Date_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    SSN_Number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    SIN_Number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    Nationality = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]'
    Country = "//span[text()='Indian']//parent::div"
    Marital_Status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]'
    Status = "//span[text()='Single']//parent::div"
    DOB_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    Gender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    Military_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    Save_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    Blood_Type = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    Blood = "//span[text()='A+']//parent::div"
    Save_Blood_Group = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    
class OrangeHRM_Contact_Details:
    # Employee_Contact_Details
    Address_street1 = "25, Kamaraj Street"
    Address_street2 = "Adyar, Thruvanmiyur"
    city = "Chennai"
    state = "Tamilnadu"
    zip = "600041"
    home_phone_number = "04434653549"
    Mobile_number = "9513687202"
    work_phone_number = "9874563210"
    email_ID = "killmonger89@gmail.com"
    other_email_ID = "goodbye40@hotmail.com"
    # Selenium Selector for Contact_Details
    Address_street1_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Address_street2_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    city_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    state_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    zip_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    country_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    India = "//span[text()='India']//parent::div"
    home_phone_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    Mobile_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    work_phone_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    email_ID_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    other_email_ID_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    
class OrangeHRM_Emergency_Contact_Details:
    # Employee_Emergency_Contact_Details
    name = "Killmonger"
    relationship = "Father"
    home_phone_number = "04431654684"
    Mobile_number = "9630351654"
    work_phone_number = "9865121207"
    # Selenium Selector for Emergency_Contact_Details
    Add_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    name_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relationship_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    home_phone_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    Mobile_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    work_phone_number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    save ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    
class OrangeHRM_Dependents:
    # Employee_Dependents_Details
    Name = "Killmonger"
    specify = "Father"
    DOB = "1970-05-05"
    # Selenium Selectors for Employee_Dependents_Details
    Add_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    Name_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relationship_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    others_XPATH = "//span[text()='Other']//parent::div"
    specify_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    DOB_XPATH ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    
class OrangeHRM_job:
    # Employee_Job_Details
    Joined_Date = "2020-05-01"
    Start_Date = "2020-05-01"
    End_Date = "2023-05-01"
    # Selenium Selector for Employee_Job_Details
    Joined_Date_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    Job_Title_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    Job_Title_Dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]/span'
    Job_Category_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    Operatives = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[9]/span'
    Sub_Unit_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]/i'
    Client_Services = "//span[text()='Client Services']//parent::div"
    Location_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i'
    HQ_CA_USA = "//span[text()='HQ - CA, USA']//parent::div"
    Employment_status_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i'
    Full_Time_Permanent = "//span[text()='Full-Time Permanent']//parent::div"
    Contract_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    Start_Date_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
    End_Date_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    # Browse = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div/div/div/div[2]/div/div[1]'
    Save_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

class OrangeHRM_Termination:
    # Termination_Details
    Termination_Date = "2023-01-02"
    Note = "Going Abroad"
    # Selenium Selector for Employee_Termination
    Terminate_Employment_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    Termination_Date_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    Termination_Reason_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[2]/i'
    Retired_XPATH = "//span[text()='Retired']//parent::div"
    Note_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
    Save_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    
class OrangeHRM_Employee_Activation:
    # Selenium Selector for Employee_Activation
    Activate_Employment_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    
    
class OrangeHRM_Salary_Details:
    # Salary_Details
    Salary_Components = "Basic Salary"
    Amount = "30000"
    Comment = "Your Salary"
    Account_Number = "47895612302145"
    Routing_Number = "548528"
    # Selenium Selector for Salary_Details
    Add_Salary_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    Salary_Components_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Pay_Grade_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    Grade_3_XPATH = "//span[text()='Grade 3']//parent::div"
    Pay_Frequency_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i'
    Monthly_XPATH ="//span[text()='Monthly']//parent::div"
    Currency_XPATH ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    Currency_Dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span'
    Amount_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    Comment_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea'
    Include_Direct_Deposit_Details_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    Account_Number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    Account_Type_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    Savings_XPATH = "//span[text()='Savings']//parent::div"
    Routing_Number_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    Salary_Amount_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    Save_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'
    Open_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[7]/div/button[2]/i'
    
class OrangeHRM_Tax_Exemptions:
    # Tax_Exemptions_Details
    Exemptions = "10"
    # Selenium Selector for Tax_Exemptions_Details
    Federal_Status_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    Single_XPATH = "//span[text()='Single']//parent::div"
    Exemptions_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    State_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]'
    Tennessee_XPATH = "//span[text()='Tennessee']//parent::div"
    State_Status_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]'
    State_Exemptions_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    Unemployment_State_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i'
    Work_State_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[2]/i'
    Save_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'