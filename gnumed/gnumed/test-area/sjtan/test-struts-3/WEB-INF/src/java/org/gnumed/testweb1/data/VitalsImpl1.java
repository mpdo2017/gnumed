/*
 * VitalsImpl1.java
 *
 * Created on September 19, 2004, 6:23 PM
 */

package org.gnumed.testweb1.data;

/**
 *
 * @author  sjtan
 */
public class VitalsImpl1 implements Vitals {
    private int diastolic,systolic, pr, rr, pefr,postpefr;
    private float wt, ht, temp;
    private String rhythm;
    /** Creates a new instance of VitalsImpl1 */
    public VitalsImpl1() {
    }
    
    public int getDiastolic() {
        return diastolic;
        
    }
    
    public float getHeight() {
        return ht;
    }
    
    public int getPrepefr() {
        return pefr;
    }
    
    public int getPr() {
        return pr;
    }
    
    public int getRr() {
        return rr;
    }
    
    public int getSystolic() {
        return systolic;
    }
    
    public float getTemp() {
        return temp;
    }
    
    public float getWeight() {
        return wt;
    }
    
    public void setDiastolic(int diastolic) {
        this.diastolic = diastolic;
    }
    
    public void setHeight(float height) {
        this.ht = ht;
    }
    
    public void setPrepefr(int pefr) {
        this.pefr = pefr;
    }
    
    public void setPr(int pr) {
        this.pr = pr;
    }
    
    public void setRr(int rr) {
        this.rr = rr;
    }
    
    public void setSystolic(int systolic) {
        this.systolic = systolic;
    }
    
    public void setTemp(float temp) {
        this.temp = temp;
    }
    
    public void setWeight(float weight) {
        this.wt = wt;
    }
    
    public String getRhytm() {
        return rhythm;
    }
    
    public void setRhytm(String rhytm) {
        this.rhythm = rhythm;
    }
    
    public int getPostpefr() {
        return postpefr;
    }
    
    public void setPostpefr(int postpefr) {
        this.postpefr = postpefr;
    }
    
}
