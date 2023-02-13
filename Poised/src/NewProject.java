import javax.swing.JOptionPane;
public class NewProject {
    int num = 0;
    int projNum = Integer.parseInt(JOptionPane.showInputDialog("Enter project number: "));
    String projName = JOptionPane.showInputDialog("Please enter the project name: ");
    String building = JOptionPane.showInputDialog("Please enter the type of building: ");
    int erfnum = Integer.parseInt(JOptionPane.showInputDialog("Please enter erf number: "));
    double totalCost = Double.parseDouble(JOptionPane.showInputDialog("Please enter the total amount for the project: "));
    double paid = Double.parseDouble(JOptionPane.showInputDialog("Please enter the amount that has been paid: "));
    String date = JOptionPane.showInputDialog("Please enter the deadline for the project YYY/MM/DD: ");
    String custname = JOptionPane.showInputDialog("Please enter customer name and surname: ");
    int custnum = Integer.parseInt(JOptionPane.showInputDialog("Please enter the customer's phone number"));
    String custEmail = JOptionPane.showInputDialog("Please enter the customer's email");
    String custAdress = JOptionPane.showInputDialog("Please enter physical address of the customer: ");
    int slocation;
    String custSurname;

    NewProject(int projNum, String projName, String building, int erfnum, double totalCost, double paid, String date, String custname, int custnum, String custEmail, String custAdress) {
        this.slocation = this.custname.indexOf(" ") + 1;
        this.custSurname = this.custname.substring(this.slocation);
    }

    public NewProject(int projNum, String projName, String building, String custAdress, int erfnum, double totalCost, double paid, String date, String custname, int custnum, String custEmail, String custAdress1) {
        this.slocation = this.custname.indexOf(" ") + 1;
        this.custSurname = this.custname.substring(this.slocation);
    }

    public double getTotalCost() {
        double sum = this.totalCost - this.paid;
        return sum;
    }

    NewProject() {
        this.slocation = this.custname.indexOf(" ") + 1;
        this.custSurname = this.custname.substring(this.slocation);
    }
}
