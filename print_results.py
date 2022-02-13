#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Ayush K.
# DATE CREATED: 12-02-2022
# REVISED DATE: 12-02-2022
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print("Model Used: {0}".format(model))
    print("Total number of images: {0}".format(results_stats_dic["n_images"]))
    print("Total number of dog images: {0}".format(results_stats_dic["n_dogs_img"]))
    print("Total number of non dog images: {0}".format(results_stats_dic["n_notdogs_img"]))
    print("Total number of label matches: {0}".format(results_stats_dic["n_match"]))
    print("Total number of correctly classified dogs: {0}".format(results_stats_dic["n_correct_dogs"]))
    print("Total number of correctly classified non dogs: {0}".format(results_stats_dic["n_correct_notdogs"]))
    print("Total number of correctly classified dog breeds: {0}".format(results_stats_dic["n_correct_breed"]))
    print("Percentage of label matches: {0}".format(results_stats_dic["pct_match"]))
    print("Percentage of correctly classified dogs: {0}".format(results_stats_dic["pct_correct_dogs"]))
    print("Percentage of correctly classified dog breed: {0}".format(results_stats_dic["pct_correct_breed"]))
    print("Percentage of correctly classified non dogs: {0}".format(results_stats_dic["pct_correct_notdogs"]))

    if print_incorrect_dogs:
      for label in results_dic.values():
        if label[3] != label[4]:
          print("{0} is a {1} dog but got misclassified as {2} dog".format(label[0], "IS-A" if label[3] else "IS-NOT-A", "IS-A" if label[4] else "IS-NOT-A"))
    
    if print_incorrect_dogs:
      for label in results_dic.values():
        if label[2] == 0 and label[3] == label[4] == 1:
          print("{0} breed got misclassified as {1}".format(label[0], label[1]))
