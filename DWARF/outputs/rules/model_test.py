def findDecision(obj): #obj[0]: perimeter_worst, obj[1]: concave_points_worst, obj[2]: area_worst, obj[3]: concave_points_mean, obj[4]: radius_worst
   # {"feature": "perimeter_worst", "instances": 398, "metric_value": 0.9661, "depth": 1}
   if obj[0] == 'Less_85.07499999999999':
      return 'B'
   elif obj[0] == 'Less_142.7':
      # {"feature": "area_worst", "instances": 109, "metric_value": 0.8614, "depth": 2}
      if obj[2] == 'Less_928.5':
         # {"feature": "concave_points_worst", "instances": 56, "metric_value": 1.0, "depth": 3}
         if obj[1] == 'Less_0.1991':
            # {"feature": "concave_points_mean", "instances": 45, "metric_value": 0.971, "depth": 4}
            if obj[3] == 'Less_0.053335':
               # {"feature": "radius_worst", "instances": 25, "metric_value": 0.795, "depth": 5}
               if obj[4] == 'Less_19.33':
                  return 'B'
               else:
                  return 'M'
            elif obj[3] == 'Greater_0.053335':
               # {"feature": "radius_worst", "instances": 20, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'Less_19.33':
                  return 'M'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[1] == 'Greater_0.1991':
            return 'M'
         elif obj[1] == 'Less_0.07628499999999999':
            return 'B'
         else:
            return 'M'
      elif obj[2] == 'Greater_928.5':
         # {"feature": "concave_points_mean", "instances": 53, "metric_value": 0.3138, "depth": 3}
         if obj[3] == 'Greater_0.053335':
            return 'M'
         elif obj[3] == 'Less_0.053335':
            # {"feature": "radius_worst", "instances": 13, "metric_value": 0.7793, "depth": 4}
            if obj[4] == 'Less_19.33':
               # {"feature": "concave_points_worst", "instances": 9, "metric_value": 0.7642, "depth": 5}
               if obj[1] == 'Less_0.1991':
                  return 'M'
               else:
                  return 'M'
            elif obj[4] == 'Greater_19.33':
               # {"feature": "concave_points_worst", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1] == 'Less_0.1991':
                  return 'M'
               else:
                  return 'M'
            else:
               return 'M'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[0] == 'Less_101.80000000000001':
      # {"feature": "concave_points_mean", "instances": 105, "metric_value": 0.316, "depth": 2}
      if obj[3] == 'Less_0.053335':
         # {"feature": "concave_points_worst", "instances": 98, "metric_value": 0.1975, "depth": 3}
         if obj[1] == 'Less_0.1991':
            # {"feature": "radius_worst", "instances": 55, "metric_value": 0.1311, "depth": 4}
            if obj[4] == 'Less_19.33':
               # {"feature": "area_worst", "instances": 54, "metric_value": 0.133, "depth": 5}
               if obj[2] == 'Less_928.5':
                  return 'B'
               else:
                  return 'M'
            elif obj[4] == 'Less_12.575':
               return 'B'
            else:
               return 'M'
         elif obj[1] == 'Less_0.07628499999999999':
            # {"feature": "area_worst", "instances": 43, "metric_value": 0.2714, "depth": 4}
            if obj[2] == 'Less_928.5':
               # {"feature": "radius_worst", "instances": 43, "metric_value": 0.2714, "depth": 5}
               if obj[4] == 'Less_19.33':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[3] == 'Greater_0.053335':
         # {"feature": "concave_points_worst", "instances": 7, "metric_value": 0.9852, "depth": 3}
         if obj[1] == 'Less_0.1991':
            # {"feature": "area_worst", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[2] == 'Less_928.5':
               # {"feature": "radius_worst", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'Less_19.33':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[1] == 'Less_0.07628499999999999':
            return 'B'
         elif obj[1] == 'Greater_0.1991':
            return 'M'
