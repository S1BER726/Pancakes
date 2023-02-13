import javax.swing.JOptionPane;
public class Contractor {
    String name = JOptionPane.showInputDialog("Enter Contractors Name: ");
    int num = Integer.parseInt(JOptionPane.showInputDialog("Enter Contractors phone number: "));
    String email = JOptionPane.showInputDialog("Enter the email address of the Contractor: ");
    String address = JOptionPane.showInputDialog("Enter the physical address of the Contractor: ");

    Contractor(String name,int num,String email,String address) {
    }

    Contractor() {
    }
}
