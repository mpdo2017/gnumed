/*
 * TestRegex.java
 *
 * Created on 8 August 2003, 08:02
 */

package quickmed.usecases.test;
import java.util.*;
import java.util.regex.*;
/**
 *
 * @author  sjtan
 */
public class TestRegex extends javax.swing.JDialog {
    
    /** Creates new form TestRegex */
    public TestRegex(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
    }
    
    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    private void initComponents() {//GEN-BEGIN:initComponents
        java.awt.GridBagConstraints gridBagConstraints;

        jLabel1 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jTextField2 = new javax.swing.JTextField();
        jToggleButton1 = new javax.swing.JToggleButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jList1 = new javax.swing.JList();

        getContentPane().setLayout(new java.awt.GridBagLayout());

        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                closeDialog(evt);
            }
        });

        jLabel1.setText("expression");
        getContentPane().add(jLabel1, new java.awt.GridBagConstraints());

        jTextField1.setText("jTextField1");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridwidth = java.awt.GridBagConstraints.REMAINDER;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        getContentPane().add(jTextField1, gridBagConstraints);

        jLabel2.setText("regex");
        getContentPane().add(jLabel2, new java.awt.GridBagConstraints());

        jTextField2.setText("jTextField2");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridwidth = java.awt.GridBagConstraints.REMAINDER;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        getContentPane().add(jTextField2, gridBagConstraints);

        jToggleButton1.setText("find");
        jToggleButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jToggleButton1ActionPerformed(evt);
            }
        });

        getContentPane().add(jToggleButton1, new java.awt.GridBagConstraints());

        jScrollPane1.setViewportView(jList1);

        getContentPane().add(jScrollPane1, new java.awt.GridBagConstraints());

        pack();
    }//GEN-END:initComponents

    private void jToggleButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jToggleButton1ActionPerformed
        // Add your handling code here:
        String text = jTextField1.getText();
        String regex = jTextField2.getText();
        java.util.regex.Pattern p = java.util.regex.Pattern.compile(regex);
        Matcher m = p.matcher(new StringBuffer(text));
        System.out.println("Groups = " + m.groupCount());
        List l = new ArrayList();
        if (!m.find()) {
            jList1.setListData( new String[] { "No match found" } );
            return;
        }
        for (int i = 0; i <= m.groupCount(); ++i) {
            l.add(m.group(i) + "\n");
        }
        jList1.setListData( l.toArray());
        System.out.println("added " + l.size() + " groups");
    }//GEN-LAST:event_jToggleButton1ActionPerformed
    
    /** Closes the dialog */
    private void closeDialog(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_closeDialog
        setVisible(false);
        dispose();
    }//GEN-LAST:event_closeDialog
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        new TestRegex(new javax.swing.JFrame(), true).show();
    }
    
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JList jList1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextField jTextField2;
    private javax.swing.JToggleButton jToggleButton1;
    // End of variables declaration//GEN-END:variables
    
}
