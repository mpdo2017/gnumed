/** Java class "drug_element.java" generated from Poseidon for UML.
 *  Poseidon for UML is developed by <A HREF="http://www.gentleware.com">Gentleware</A>.
 *  Generated with <A HREF="http://jakarta.apache.org/velocity/">velocity</A> template engine.
 */
package org.drugref;

import java.util.*;

/**
 * <p>
 * 
 * </p>
 */
public class drug_element {

  ///////////////////////////////////////
  // attributes


/**
 * <p>
 * Represents ...
 * </p>
 */
    private Integer id; 

/**
 * <p>
 * Represents ...
 * </p>
 */
    private char category; 

/**
 * <p>
 * Represents ...
 * </p>
 */
    private String description; 

   ///////////////////////////////////////
   // associations

/**
 * <p>
 * 
 * </p>
 */
    public Collection atc = new TreeSet(); // of type atc
/**
 * <p>
 * 
 * </p>
 */
    public Collection drug = new TreeSet(); // of type drug_element
/**
 * <p>
 * 
 * </p>
 */
    public Collection class = new TreeSet(); // of type drug_element
/**
 * <p>
 * 
 * </p>
 */
    public Collection drug_warning = new TreeSet(); // of type drug_warning
/**
 * <p>
 * 
 * </p>
 */
    public Collection drug_information = new TreeSet(); // of type drug_information
/**
 * <p>
 * 
 * </p>
 */
    public Collection link_drug_interactions = new TreeSet(); // of type link_drug_interactions
/**
 * <p>
 * 
 * </p>
 */
    public Collection link_drug_interactions_1 = new TreeSet(); // of type link_drug_interactions
/**
 * <p>
 * 
 * </p>
 */
    public Collection link_drug_indication = new TreeSet(); // of type link_drug_indication
/**
 * <p>
 * 
 * </p>
 */
    public Collection product = new TreeSet(); // of type product
/**
 * <p>
 * 
 * </p>
 */
    public Collection link_drug_disease_interactions = new TreeSet(); // of type link_drug_disease_interactions


   ///////////////////////////////////////
   // access methods for associations

    public Collection getAtcs() {
        return atc;
    }
    public void addAtc(atc _atc) {
        if (! this.atc.contains(_atc)) {
            this.atc.add(_atc);
            _atc.addDrug_element(this);
        }
    }
    public void removeAtc(atc _atc) {
        boolean removed = this.atc.remove(_atc);
        if (removed) _atc.removeDrug_element(this);
    }
    public Collection getDrugs() {
        return drug;
    }
    public void addDrug(drug_element _drug_element) {
        if (! this.drug.contains(_drug_element)) {
            this.drug.add(_drug_element);
            _drug_element.addClass(this);
        }
    }
    public void removeDrug(drug_element _drug_element) {
        boolean removed = this.drug.remove(_drug_element);
        if (removed) _drug_element.removeClass(this);
    }
    public Collection getClasss() {
        return class;
    }
    public void addClass(drug_element _drug_element) {
        if (! this.class.contains(_drug_element)) {
            this.class.add(_drug_element);
            _drug_element.addDrug(this);
        }
    }
    public void removeClass(drug_element _drug_element) {
        boolean removed = this.class.remove(_drug_element);
        if (removed) _drug_element.removeDrug(this);
    }
    public Collection getDrug_warnings() {
        return drug_warning;
    }
    public void addDrug_warning(drug_warning _drug_warning) {
        if (! this.drug_warning.contains(_drug_warning)) {
            this.drug_warning.add(_drug_warning);
            _drug_warning.addDrug_element(this);
        }
    }
    public void removeDrug_warning(drug_warning _drug_warning) {
        boolean removed = this.drug_warning.remove(_drug_warning);
        if (removed) _drug_warning.removeDrug_element(this);
    }
    public Collection getDrug_informations() {
        return drug_information;
    }
    public void addDrug_information(drug_information _drug_information) {
        if (! this.drug_information.contains(_drug_information)) {
            this.drug_information.add(_drug_information);
            _drug_information.addDrug_element(this);
        }
    }
    public void removeDrug_information(drug_information _drug_information) {
        boolean removed = this.drug_information.remove(_drug_information);
        if (removed) _drug_information.removeDrug_element(this);
    }
    public Collection getLink_drug_interactionss() {
        return link_drug_interactions;
    }
    public void addLink_drug_interactions(link_drug_interactions _link_drug_interactions) {
        if (! this.link_drug_interactions.contains(_link_drug_interactions)) {
            this.link_drug_interactions.add(_link_drug_interactions);
            _link_drug_interactions.setInteractor(this);
        }
    }
    public void removeLink_drug_interactions(link_drug_interactions _link_drug_interactions) {
        boolean removed = this.link_drug_interactions.remove(_link_drug_interactions);
        if (removed) _link_drug_interactions.setInteractor((drug_element)null);
    }
    public Collection getLink_drug_interactions_1s() {
        return link_drug_interactions_1;
    }
    public void addLink_drug_interactions_1(link_drug_interactions _link_drug_interactions) {
        if (! this.link_drug_interactions_1.contains(_link_drug_interactions)) {
            this.link_drug_interactions_1.add(_link_drug_interactions);
            _link_drug_interactions.setDrug_element(this);
        }
    }
    public void removeLink_drug_interactions_1(link_drug_interactions _link_drug_interactions) {
        boolean removed = this.link_drug_interactions_1.remove(_link_drug_interactions);
        if (removed) _link_drug_interactions.setDrug_element((drug_element)null);
    }
    public Collection getLink_drug_indications() {
        return link_drug_indication;
    }
    public void addLink_drug_indication(link_drug_indication _link_drug_indication) {
        if (! this.link_drug_indication.contains(_link_drug_indication)) {
            this.link_drug_indication.add(_link_drug_indication);
            _link_drug_indication.setDrug_element(this);
        }
    }
    public void removeLink_drug_indication(link_drug_indication _link_drug_indication) {
        boolean removed = this.link_drug_indication.remove(_link_drug_indication);
        if (removed) _link_drug_indication.setDrug_element((drug_element)null);
    }
    public Collection getProducts() {
        return product;
    }
    public void addProduct(product _product) {
        if (! this.product.contains(_product)) {
            this.product.add(_product);
            _product.setDrug_element(this);
        }
    }
    public void removeProduct(product _product) {
        boolean removed = this.product.remove(_product);
        if (removed) _product.setDrug_element((drug_element)null);
    }
    public Collection getLink_drug_disease_interactionss() {
        return link_drug_disease_interactions;
    }
    public void addLink_drug_disease_interactions(link_drug_disease_interactions _link_drug_disease_interactions) {
        if (! this.link_drug_disease_interactions.contains(_link_drug_disease_interactions)) {
            this.link_drug_disease_interactions.add(_link_drug_disease_interactions);
            _link_drug_disease_interactions.setDrug_element(this);
        }
    }
    public void removeLink_drug_disease_interactions(link_drug_disease_interactions _link_drug_disease_interactions) {
        boolean removed = this.link_drug_disease_interactions.remove(_link_drug_disease_interactions);
        if (removed) _link_drug_disease_interactions.setDrug_element((drug_element)null);
    }


  ///////////////////////////////////////
  // operations


/**
 * <p>
 * Represents ...
 * </p>
 */
    public Integer getId() {        
        return id;
    } // end getId        

/**
 * <p>
 * Represents ...
 * </p>
 */
    public void setId(Integer _id) {        
        id = _id;
    } // end setId        

/**
 * <p>
 * Represents ...
 * </p>
 */
    public char getCategory() {        
        return category;
    } // end getCategory        

/**
 * <p>
 * Represents ...
 * </p>
 */
    public void setCategory(char _category) {        
        category = _category;
    } // end setCategory        

/**
 * <p>
 * Represents ...
 * </p>
 */
    public String getDescription() {        
        return description;
    } // end getDescription        

/**
 * <p>
 * Represents ...
 * </p>
 */
    public void setDescription(String _description) {        
        description = _description;
    } // end setDescription        

} // end drug_element





