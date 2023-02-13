// import javax.swing.*;
import javax.swing.JOptionPane;

public class Architect {
    String name = JOptionPane.showInputDialog("Enter Architects Name: ");
    int num = Integer.parseInt(JOptionPane.showInputDialog("Enter Architects phone number: "));
    String email = JOptionPane.showInputDialog("Enter the email address of the Architect: ");
    String address = JOptionPane.showInputDialog("Enter the physical address of the Architect: ");

    Architect(String name,int num,String email,String address) {
    }

    Architect() {
    }

}
