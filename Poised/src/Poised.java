import javax.swing.JOptionPane;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Poised {
    public static void main(String args[]) {
        NewProject[] pobj = new NewProject[5];
        int projNum = 0;

        Contractor[] cobj = new Contractor[5];
        int cnum = 0;

        String timestamp = new SimpleDateFormat("yyyMMdd").format(Calendar.getInstance().getTime());
        char option = JOptionPane.showInputDialog("MAIN MENU,Please choose an option from below: \n A) Create a new a project \n" +
                "B) Edit \n C) Finalize a project \n D) Exit").toLowerCase().charAt(0);

        // Create a loop for the menu to keep showing
        // as long as the user has not exited
        while (option != 'd') {


            if (option == 'a') {
                if (projNum > 4) {
                    System.out.println("You cannot add any more projects.Please complete the projects and try again");
                } else {
                    NewProject plink = new NewProject();
                    pobj[projNum] = new NewProject(plink.projNum, plink.projName, plink.building, plink.custAdress, plink.erfnum, plink.totalCost, plink.paid, plink.date, plink.custname, plink.custnum, plink.custEmail, plink.custAdress);
                    System.out.println("Your project has been added and your project number is" + projNum);
                    projNum++;
                }
            }
            if (option == 'b') {
                char option2 = JOptionPane.showInputDialog("What would you like to edit?" + "\nA) Project Due Date" + "\nB) Total cost of the project" + "\nC) Contractors information" + "\nD) Exit").toLowerCase().charAt(0);
                while (option2 != 'd') {
                    int projnum2 = Integer.parseInt(JOptionPane.showInputDialog("Enter the project you want to edit"));
                    if (option2 == 'a') {
                        if (pobj[projnum2].date.isEmpty()) {
                            System.out.println("This project does not exist");
                        } else {
                            String change = JOptionPane.showInputDialog("Please enter the new due date YYYY/MM/DD");
                            System.out.println("The project due date has been changed");
                            System.out.println("Old due date: " + pobj[projnum2].date);
                            pobj[projnum2].date = change;
                            System.out.println("New Due Date: " + pobj[projnum2].date);
                        }
                    }
                    if (option2 == 'b') {
                        double change = Double.parseDouble(JOptionPane.showInputDialog("Enter the new amount"));

                        System.out.println("The total cost of the project has been changed");
                        System.out.println("Old cost R " + pobj[projnum2].totalCost);
                        pobj[projnum2].totalCost = change;
                        System.out.println("New cost R " + pobj[projnum2].totalCost);
                    }

                    if (option2 == 'c') {
                        cobj[projnum2].name = JOptionPane.showInputDialog("Enter new Contractor name");
                        cobj[projnum2].num = Integer.parseInt(JOptionPane.showInputDialog("Enter new Contractor phone number"));
                        cobj[projnum2].email = JOptionPane.showInputDialog("Enter new Contractor email address");
                        cobj[projnum2].address = JOptionPane.showInputDialog("Enter new Contractor physical address");
                    }
                }
            }
            if (option == 'c') {
                int projnum = Integer.parseInt(JOptionPane.showInputDialog("Please enter the project you would like to finalize:"));
                if (pobj[projnum].getTotalCost() > 0.00) {

                    System.out.println("You have an outstanding balance of R" + pobj[projnum].getTotalCost());
                    System.out.println("You have an outstanding balance of R" + pobj[projnum].getTotalCost() + "\n");
                    System.out.println("Name: " + pobj[projnum].custname + "\n");
                    System.out.println("Email: " + pobj[projnum].custEmail + "\n");
                    System.out.println("Phone Number: " + pobj[projnum].custnum + "\n");
                    System.out.println("Address: " + pobj[projnum].custAdress + "\n");
                    System.out.println("Project Number: " + pobj[projnum].projNum + "\n");
                    System.out.println("Project Name: " + pobj[projnum].projName + "\n");
                    System.out.println("Building Type: " + pobj[projnum].building + "\n");
                    System.out.println(" ERF Number: " + pobj[projnum].erfnum + "\n");
                    System.out.println("Total Cost: " + pobj[projnum].totalCost + "\n");
                    System.out.println("Deadline: " + pobj[projnum].date + "\n");
                    // YYYYMMDD format
                    System.out.print(timestamp);
                    System.out.println(" ");

                } else {
                    System.out.println("You have an outstanding balance of R" + pobj[projnum].getTotalCost() + "\n");
                    System.out.println("Name: " + pobj[projnum].custname + "\n");
                    System.out.println("Email: " + pobj[projnum].custEmail + "\n");
                    System.out.println("Phone Number: " + pobj[projnum].custnum + "\n");
                    System.out.println("Address: " + pobj[projnum].custAdress + "\n");
                    System.out.println("Project Number: " + pobj[projnum].projNum + "\n");
                    System.out.println("Project Name: " + pobj[projnum].projName + "\n");
                    System.out.println("Building Type: " + pobj[projnum].building + "\n");
                    System.out.println(" ERF Number: " + pobj[projnum].erfnum + "\n");
                    System.out.println("Total Cost: " + pobj[projnum].totalCost + "\n");
                    System.out.println("Deadline: " + pobj[projnum].date + "\n");
                    // YYYYMMDD format
                    System.out.print(timestamp);
                    System.out.println(" ");
                }
                option = JOptionPane.showInputDialog("MAIN MENU:" + "\nA) Add project" + "\nB) Add Contractor" + "\nC) Finalize a project" + "\nD) Edit" + "\nE) Exit").toLowerCase().charAt(0);

            }

        }
    }
    }

