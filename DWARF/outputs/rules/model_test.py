def findDecision(obj): #obj[0]: alcohol, obj[1]: sulphates, obj[2]: volatile acidity, obj[3]: total sulfur dioxide, obj[4]: density, obj[5]: chlorides, obj[6]: pH
   # {"feature": "alcohol", "instances": 1599, "metric_value": 0.9965, "depth": 1}
   if obj[0] == 'Greater_10.725':
      # {"feature": "sulphates", "instances": 559, "metric_value": 0.7226, "depth": 2}
      if obj[1] == 'Less_1.35':
         # {"feature": "chlorides", "instances": 269, "metric_value": 0.4583, "depth": 3}
         if obj[5] == 'Less_0.0765':
            # {"feature": "total sulfur dioxide", "instances": 159, "metric_value": 0.2605, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "volatile acidity", "instances": 87, "metric_value": 0.2691, "depth": 5}
               if obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               elif obj[2] == 'Greater_0.6975':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "volatile acidity", "instances": 22, "metric_value": 0.4395, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               elif obj[2] == 'Greater_0.6975':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               # {"feature": "volatile acidity", "instances": 21, "metric_value": 0.2762, "depth": 5}
               if obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[5] == 'Less_0.0985':
            # {"feature": "total sulfur dioxide", "instances": 79, "metric_value": 0.6451, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "volatile acidity", "instances": 33, "metric_value": 0.5328, "depth": 5}
               if obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               elif obj[2] == 'Greater_0.6975':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "density", "instances": 18, "metric_value": 0.3095, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "pH", "instances": 17, "metric_value": 0.9975, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'good'
               elif obj[6] == 'Less_3.145':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               return 'good'
            else:
               return 'good'
         elif obj[5] == 'Greater_0.0985':
            # {"feature": "volatile acidity", "instances": 31, "metric_value": 0.7088, "depth": 4}
            if obj[2] == 'Less_0.5625':
               # {"feature": "pH", "instances": 14, "metric_value": 0.9852, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Less_3.145':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.3675':
               return 'good'
            elif obj[2] == 'Less_0.6975':
               return 'good'
            elif obj[2] == 'Greater_0.6975':
               return 'good'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[1] == 'Less_0.655':
         # {"feature": "volatile acidity", "instances": 260, "metric_value": 0.8993, "depth": 3}
         if obj[2] == 'Less_0.5625':
            # {"feature": "pH", "instances": 89, "metric_value": 0.8244, "depth": 4}
            if obj[6] == 'Less_3.455':
               # {"feature": "density", "instances": 57, "metric_value": 0.67, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Greater_3.455':
               # {"feature": "density", "instances": 20, "metric_value": 0.9928, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               # {"feature": "total sulfur dioxide", "instances": 12, "metric_value": 0.65, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'good'
               elif obj[3] == 'Less_44.5':
                  return 'bad'
               elif obj[3] == 'Greater_64.5':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[2] == 'Greater_0.6975':
            # {"feature": "density", "instances": 59, "metric_value": 0.9948, "depth": 4}
            if obj[4] == 'Less_0.9967900000000001':
               # {"feature": "chlorides", "instances": 53, "metric_value": 0.9997, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Less_0.0985':
                  return 'bad'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Greater_0.9967900000000001':
               return 'bad'
            else:
               return 'good'
         elif obj[2] == 'Less_0.3675':
            # {"feature": "pH", "instances": 57, "metric_value": 0.3666, "depth": 4}
            if obj[6] == 'Less_3.455':
               # {"feature": "density", "instances": 44, "metric_value": 0.3591, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               return 'good'
            elif obj[6] == 'Greater_3.455':
               # {"feature": "total sulfur dioxide", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Less_44.5':
                  return 'good'
               elif obj[3] == 'Greater_64.5':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[2] == 'Less_0.6975':
            # {"feature": "pH", "instances": 55, "metric_value": 0.9806, "depth": 4}
            if obj[6] == 'Less_3.455':
               # {"feature": "chlorides", "instances": 36, "metric_value": 0.9183, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'bad'
               elif obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Greater_3.455':
               # {"feature": "total sulfur dioxide", "instances": 16, "metric_value": 1.0, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Greater_64.5':
                  return 'good'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               return 'bad'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[1] == 'Less_0.675':
         # {"feature": "total sulfur dioxide", "instances": 30, "metric_value": 0.5665, "depth": 3}
         if obj[3] == 'Less_35.5':
            # {"feature": "pH", "instances": 19, "metric_value": 0.2975, "depth": 4}
            if obj[6] == 'Less_3.455':
               return 'good'
            elif obj[6] == 'Greater_3.455':
               # {"feature": "density", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               return 'good'
            else:
               return 'good'
         elif obj[3] == 'Less_44.5':
            # {"feature": "volatile acidity", "instances": 6, "metric_value": 0.65, "depth": 4}
            if obj[2] == 'Less_0.3675':
               return 'good'
            elif obj[2] == 'Less_0.5625':
               # {"feature": "density", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.6975':
               return 'good'
            else:
               return 'good'
         elif obj[3] == 'Greater_64.5':
            # {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[6] == 'Less_3.455':
               return 'bad'
            elif obj[6] == 'Greater_3.455':
               return 'good'
            else:
               return 'good'
         elif obj[3] == 'Less_64.5':
            return 'good'
         else:
            return 'good'
      else:
         return 'good'
   elif obj[0] == 'Less_9.525':
      # {"feature": "sulphates", "instances": 436, "metric_value": 0.8614, "depth": 2}
      if obj[1] == 'Less_0.655':
         # {"feature": "total sulfur dioxide", "instances": 324, "metric_value": 0.7859, "depth": 3}
         if obj[3] == 'Greater_64.5':
            # {"feature": "chlorides", "instances": 139, "metric_value": 0.6125, "depth": 4}
            if obj[5] == 'Less_0.0985':
               # {"feature": "pH", "instances": 81, "metric_value": 0.6052, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Less_3.145':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'bad'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.0765':
               # {"feature": "pH", "instances": 34, "metric_value": 0.8338, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'bad'
               else:
                  return 'good'
            elif obj[5] == 'Greater_0.0985':
               return 'bad'
            else:
               return 'good'
         elif obj[3] == 'Less_35.5':
            # {"feature": "pH", "instances": 100, "metric_value": 0.9044, "depth": 4}
            if obj[6] == 'Less_3.455':
               # {"feature": "density", "instances": 79, "metric_value": 0.9005, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               # {"feature": "chlorides", "instances": 13, "metric_value": 0.9957, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Less_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Greater_3.455':
               return 'bad'
            else:
               return 'good'
         elif obj[3] == 'Less_64.5':
            # {"feature": "pH", "instances": 43, "metric_value": 0.8841, "depth": 4}
            if obj[6] == 'Less_3.455':
               # {"feature": "chlorides", "instances": 32, "metric_value": 0.8571, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'bad'
               elif obj[5] == 'Less_0.0765':
                  return 'bad'
               elif obj[5] == 'Greater_0.0985':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Greater_3.455':
               # {"feature": "density", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.145':
               return 'bad'
            else:
               return 'good'
         elif obj[3] == 'Less_44.5':
            # {"feature": "chlorides", "instances": 42, "metric_value": 0.7919, "depth": 4}
            if obj[5] == 'Less_0.0765':
               # {"feature": "volatile acidity", "instances": 21, "metric_value": 0.4537, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'bad'
               elif obj[2] == 'Greater_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.3675':
                  return 'bad'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.0985':
               # {"feature": "density", "instances": 19, "metric_value": 0.9819, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Greater_0.0985':
               return 'bad'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[1] == 'Less_1.35':
         # {"feature": "chlorides", "instances": 94, "metric_value": 0.979, "depth": 3}
         if obj[5] == 'Greater_0.0985':
            # {"feature": "volatile acidity", "instances": 46, "metric_value": 0.6666, "depth": 4}
            if obj[2] == 'Less_0.5625':
               # {"feature": "total sulfur dioxide", "instances": 24, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Greater_64.5':
                  return 'bad'
               elif obj[3] == 'Less_64.5':
                  return 'bad'
               elif obj[3] == 'Less_44.5':
                  return 'bad'
               elif obj[3] == 'Less_35.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.6975':
               return 'bad'
            elif obj[2] == 'Greater_0.6975':
               # {"feature": "total sulfur dioxide", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[3] == 'Greater_64.5':
                  return 'bad'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.3675':
               # {"feature": "total sulfur dioxide", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[5] == 'Less_0.0985':
            # {"feature": "total sulfur dioxide", "instances": 28, "metric_value": 0.9403, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "volatile acidity", "instances": 14, "metric_value": 0.5917, "depth": 5}
               if obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               elif obj[2] == 'Greater_0.6975':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "volatile acidity", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Greater_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.3675':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "density", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[5] == 'Less_0.0765':
            # {"feature": "volatile acidity", "instances": 20, "metric_value": 0.9341, "depth": 4}
            if obj[2] == 'Less_0.6975':
               # {"feature": "total sulfur dioxide", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Less_44.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.3675':
               return 'good'
            elif obj[2] == 'Less_0.5625':
               # {"feature": "density", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[2] == 'Greater_0.6975':
               return 'good'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[1] == 'Less_0.675':
         # {"feature": "total sulfur dioxide", "instances": 13, "metric_value": 0.9612, "depth": 3}
         if obj[3] == 'Less_35.5':
            # {"feature": "volatile acidity", "instances": 9, "metric_value": 0.5033, "depth": 4}
            if obj[2] == 'Less_0.6975':
               return 'good'
            elif obj[2] == 'Less_0.3675':
               # {"feature": "chlorides", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Less_0.0765':
                  return 'bad'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.5625':
               return 'good'
            else:
               return 'good'
         elif obj[3] == 'Greater_64.5':
            return 'bad'
         elif obj[3] == 'Less_64.5':
            return 'bad'
         else:
            return 'good'
      elif obj[1] == 'Greater_1.35':
         # {"feature": "density", "instances": 5, "metric_value": 0.7219, "depth": 3}
         if obj[4] == 'Less_0.9967900000000001':
            # {"feature": "volatile acidity", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[2] == 'Greater_0.6975':
               return 'bad'
            elif obj[2] == 'Less_0.6975':
               return 'good'
            elif obj[2] == 'Less_0.3675':
               return 'bad'
            else:
               return 'good'
         elif obj[4] == 'Greater_0.9967900000000001':
            return 'bad'
         else:
            return 'good'
      else:
         return 'good'
   elif obj[0] == 'Less_10.066666665':
      # {"feature": "volatile acidity", "instances": 313, "metric_value": 0.9511, "depth": 2}
      if obj[2] == 'Less_0.6975':
         # {"feature": "sulphates", "instances": 109, "metric_value": 0.8954, "depth": 3}
         if obj[1] == 'Less_0.655':
            # {"feature": "total sulfur dioxide", "instances": 76, "metric_value": 0.8997, "depth": 4}
            if obj[3] == 'Greater_64.5':
               # {"feature": "chlorides", "instances": 36, "metric_value": 0.888, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'bad'
               elif obj[5] == 'Less_0.0765':
                  return 'bad'
               elif obj[5] == 'Greater_0.0985':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_35.5':
               # {"feature": "chlorides", "instances": 26, "metric_value": 0.9957, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               return 'bad'
            elif obj[3] == 'Less_44.5':
               # {"feature": "chlorides", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'bad'
               elif obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_1.35':
            # {"feature": "total sulfur dioxide", "instances": 21, "metric_value": 0.9984, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "chlorides", "instances": 12, "metric_value": 1.0, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'bad'
               elif obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               # {"feature": "pH", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[6] == 'Less_3.145':
                  return 'good'
               elif obj[6] == 'Less_3.455':
                  return 'good'
               elif obj[6] == 'Greater_3.455':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               return 'bad'
            elif obj[3] == 'Less_64.5':
               return 'bad'
            else:
               return 'good'
         elif obj[1] == 'Less_0.675':
            return 'bad'
         else:
            return 'good'
      elif obj[2] == 'Less_0.5625':
         # {"feature": "sulphates", "instances": 107, "metric_value": 0.9994, "depth": 3}
         if obj[1] == 'Less_0.655':
            # {"feature": "total sulfur dioxide", "instances": 68, "metric_value": 0.9367, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "pH", "instances": 31, "metric_value": 0.9629, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Less_3.145':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "density", "instances": 15, "metric_value": 0.5665, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "pH", "instances": 12, "metric_value": 1.0, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'good'
               elif obj[6] == 'Less_3.145':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               # {"feature": "pH", "instances": 10, "metric_value": 0.971, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'good'
               elif obj[6] == 'Greater_3.455':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_1.35':
            # {"feature": "total sulfur dioxide", "instances": 33, "metric_value": 0.8454, "depth": 4}
            if obj[3] == 'Less_64.5':
               # {"feature": "chlorides", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_35.5':
               # {"feature": "density", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "chlorides", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'bad'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               elif obj[5] == 'Less_0.0765':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[1] == 'Greater_1.35':
            # {"feature": "total sulfur dioxide", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Greater_64.5':
               # {"feature": "density", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_0.675':
            # {"feature": "total sulfur dioxide", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Less_44.5':
               # {"feature": "chlorides", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[5] == 'Less_0.0985':
                  return 'good'
               elif obj[5] == 'Greater_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               return 'good'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[2] == 'Greater_0.6975':
         # {"feature": "pH", "instances": 68, "metric_value": 0.5639, "depth": 3}
         if obj[6] == 'Less_3.455':
            # {"feature": "total sulfur dioxide", "instances": 52, "metric_value": 0.6647, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "sulphates", "instances": 31, "metric_value": 0.4587, "depth": 5}
               if obj[1] == 'Less_0.655':
                  return 'bad'
               elif obj[1] == 'Less_0.675':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "density", "instances": 13, "metric_value": 0.6194, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "density", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               return 'good'
            else:
               return 'good'
         elif obj[6] == 'Greater_3.455':
            return 'bad'
         elif obj[6] == 'Less_3.145':
            return 'bad'
         else:
            return 'good'
      elif obj[2] == 'Less_0.3675':
         # {"feature": "sulphates", "instances": 29, "metric_value": 0.8498, "depth": 3}
         if obj[1] == 'Less_1.35':
            # {"feature": "chlorides", "instances": 19, "metric_value": 0.8315, "depth": 4}
            if obj[5] == 'Less_0.0985':
               # {"feature": "pH", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[6] == 'Less_3.455':
                  return 'bad'
               elif obj[6] == 'Greater_3.455':
                  return 'bad'
               elif obj[6] == 'Less_3.145':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.0765':
               return 'good'
            elif obj[5] == 'Greater_0.0985':
               return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_0.655':
            # {"feature": "total sulfur dioxide", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[3] == 'Less_64.5':
               # {"feature": "density", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               return 'bad'
            elif obj[3] == 'Less_44.5':
               return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_0.675':
            return 'good'
         elif obj[1] == 'Greater_1.35':
            return 'good'
         else:
            return 'good'
      else:
         return 'good'
   elif obj[0] == 'Less_10.725':
      # {"feature": "pH", "instances": 291, "metric_value": 0.9827, "depth": 2}
      if obj[6] == 'Less_3.455':
         # {"feature": "sulphates", "instances": 223, "metric_value": 0.9589, "depth": 3}
         if obj[1] == 'Less_0.655':
            # {"feature": "chlorides", "instances": 141, "metric_value": 0.9895, "depth": 4}
            if obj[5] == 'Less_0.0985':
               # {"feature": "total sulfur dioxide", "instances": 86, "metric_value": 0.9431, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'good'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               elif obj[3] == 'Less_44.5':
                  return 'good'
               elif obj[3] == 'Greater_64.5':
                  return 'bad'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.0765':
               # {"feature": "density", "instances": 42, "metric_value": 0.9852, "depth": 5}
               if obj[4] == 'Less_0.9967900000000001':
                  return 'bad'
               elif obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Greater_0.0985':
               # {"feature": "total sulfur dioxide", "instances": 13, "metric_value": 0.9957, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Greater_64.5':
                  return 'good'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_1.35':
            # {"feature": "total sulfur dioxide", "instances": 72, "metric_value": 0.8709, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "density", "instances": 35, "metric_value": 0.5917, "depth": 5}
               if obj[4] == 'Greater_0.9967900000000001':
                  return 'good'
               elif obj[4] == 'Less_0.9967900000000001':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Greater_64.5':
               # {"feature": "chlorides", "instances": 19, "metric_value": 0.8997, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'bad'
               elif obj[5] == 'Less_0.0985':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "volatile acidity", "instances": 15, "metric_value": 0.7219, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'good'
               elif obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               return 'good'
            else:
               return 'good'
         elif obj[1] == 'Less_0.675':
            # {"feature": "total sulfur dioxide", "instances": 9, "metric_value": 0.7642, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "chlorides", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[5] == 'Less_0.0765':
                  return 'good'
               elif obj[5] == 'Less_0.0985':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               return 'good'
            elif obj[3] == 'Greater_64.5':
               return 'bad'
            else:
               return 'good'
         elif obj[1] == 'Greater_1.35':
            return 'good'
         else:
            return 'good'
      elif obj[6] == 'Greater_3.455':
         # {"feature": "chlorides", "instances": 37, "metric_value": 0.974, "depth": 3}
         if obj[5] == 'Less_0.0985':
            # {"feature": "total sulfur dioxide", "instances": 21, "metric_value": 0.7919, "depth": 4}
            if obj[3] == 'Less_35.5':
               # {"feature": "volatile acidity", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[2] == 'Less_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.5625':
                  return 'bad'
               elif obj[2] == 'Greater_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.3675':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_44.5':
               # {"feature": "sulphates", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[1] == 'Less_0.655':
                  return 'good'
               elif obj[1] == 'Less_0.675':
                  return 'bad'
               else:
                  return 'good'
            elif obj[3] == 'Less_64.5':
               # {"feature": "sulphates", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1] == 'Less_0.655':
                  return 'bad'
               elif obj[1] == 'Less_1.35':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[5] == 'Less_0.0765':
            # {"feature": "volatile acidity", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[2] == 'Less_0.6975':
               # {"feature": "sulphates", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1] == 'Less_0.655':
                  return 'bad'
               elif obj[1] == 'Less_1.35':
                  return 'bad'
               else:
                  return 'good'
            elif obj[2] == 'Greater_0.6975':
               # {"feature": "total sulfur dioxide", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Greater_64.5':
                  return 'bad'
               elif obj[3] == 'Less_64.5':
                  return 'good'
               elif obj[3] == 'Less_35.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.5625':
               return 'good'
            elif obj[2] == 'Less_0.3675':
               return 'good'
            else:
               return 'good'
         elif obj[5] == 'Greater_0.0985':
            # {"feature": "sulphates", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[1] == 'Less_0.655':
               return 'good'
            elif obj[1] == 'Less_1.35':
               return 'bad'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[6] == 'Less_3.145':
         # {"feature": "sulphates", "instances": 31, "metric_value": 0.9992, "depth": 3}
         if obj[1] == 'Less_1.35':
            # {"feature": "chlorides", "instances": 15, "metric_value": 0.971, "depth": 4}
            if obj[5] == 'Less_0.0765':
               # {"feature": "volatile acidity", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.5625':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.0985':
               # {"feature": "volatile acidity", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'bad'
               elif obj[2] == 'Less_0.3675':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Greater_0.0985':
               return 'bad'
            else:
               return 'good'
         elif obj[1] == 'Less_0.655':
            # {"feature": "density", "instances": 14, "metric_value": 0.9403, "depth": 4}
            if obj[4] == 'Greater_0.9967900000000001':
               # {"feature": "volatile acidity", "instances": 12, "metric_value": 0.8113, "depth": 5}
               if obj[2] == 'Less_0.5625':
                  return 'bad'
               elif obj[2] == 'Greater_0.6975':
                  return 'good'
               elif obj[2] == 'Less_0.6975':
                  return 'bad'
               elif obj[2] == 'Less_0.3675':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Less_0.9967900000000001':
               return 'good'
            else:
               return 'good'
         elif obj[1] == 'Greater_1.35':
            return 'good'
         elif obj[1] == 'Less_0.675':
            return 'bad'
         else:
            return 'good'
      else:
         return 'good'
   else:
      return 'good'
