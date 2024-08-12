def findDecision(obj): #obj[0]: radius_worst, obj[1]: area_worst, obj[2]: concave_points_mean, obj[3]: concave_points_worst, obj[4]: concavity_mean, obj[5]: radius_mean
   # {"feature": "radius_worst", "instances": 569, "metric_value": 0.1413, "depth": 1}
   if obj[0] == 'Less_16.355':
      # {"feature": "concave_points_worst", "instances": 224, "metric_value": 0.0947, "depth": 2}
      if obj[3] == 'Less_0.14205':
         # {"feature": "concave_points_mean", "instances": 196, "metric_value": 0.0634, "depth": 3}
         if obj[2] == 'Less_0.02388':
            # {"feature": "area_worst", "instances": 92, "metric_value": 0.0206, "depth": 4}
            if obj[1] == 'Less_674.95':
               return 'B'
            elif obj[1] == 'Less_1320.5':
               # {"feature": "concavity_mean", "instances": 19, "metric_value": 0.0987, "depth": 5}
               if obj[4] == 'Less_0.034460000000000005':
                  return 'B'
               elif obj[4] == 'Less_0.2096':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[2] == 'Less_0.04877':
            # {"feature": "radius_mean", "instances": 87, "metric_value": 0.0644, "depth": 4}
            if obj[5] == 'Less_12.855':
               # {"feature": "concavity_mean", "instances": 40, "metric_value": 0.0913, "depth": 5}
               if obj[4] == 'Less_0.2096':
                  return 'B'
               elif obj[4] == 'Less_0.034460000000000005':
                  return 'B'
               else:
                  return 'M'
            elif obj[5] == 'Less_14.370000000000001':
               return 'B'
            elif obj[5] == 'Greater_14.370000000000001':
               # {"feature": "concavity_mean", "instances": 10, "metric_value": 0.1667, "depth": 5}
               if obj[4] == 'Less_0.034460000000000005':
                  return 'B'
               elif obj[4] == 'Less_0.2096':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[2] == 'Greater_0.05418':
            # {"feature": "radius_mean", "instances": 10, "metric_value": 0.15, "depth": 4}
            if obj[5] == 'Less_14.370000000000001':
               # {"feature": "area_worst", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[1] == 'Less_674.95':
                  return 'B'
               elif obj[1] == 'Less_1320.5':
                  return 'M'
               else:
                  return 'M'
            elif obj[5] == 'Greater_14.370000000000001':
               return 'B'
            elif obj[5] == 'Less_12.855':
               return 'B'
            else:
               return 'M'
         elif obj[2] == 'Less_0.05418':
            # {"feature": "area_worst", "instances": 7, "metric_value": 0.1905, "depth": 4}
            if obj[1] == 'Less_674.95':
               return 'B'
            elif obj[1] == 'Less_1320.5':
               # {"feature": "concavity_mean", "instances": 3, "metric_value": 0.4444, "depth": 5}
               if obj[4] == 'Less_0.2096':
                  return 'M'
               else:
                  return 'M'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[3] == 'Greater_0.1611':
         # {"feature": "area_worst", "instances": 16, "metric_value": 0.0938, "depth": 3}
         if obj[1] == 'Less_1320.5':
            return 'M'
         elif obj[1] == 'Less_674.95':
            # {"feature": "radius_mean", "instances": 4, "metric_value": 0.0, "depth": 4}
            if obj[5] == 'Less_12.855':
               return 'M'
            elif obj[5] == 'Less_14.370000000000001':
               return 'B'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[3] == 'Less_0.1611':
         # {"feature": "radius_mean", "instances": 12, "metric_value": 0.4107, "depth": 3}
         if obj[5] == 'Less_14.370000000000001':
            # {"feature": "concave_points_mean", "instances": 7, "metric_value": 0.3333, "depth": 4}
            if obj[2] == 'Greater_0.05418':
               # {"feature": "concavity_mean", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'Less_0.2096':
                  return 'M'
               elif obj[4] == 'Greater_0.26385000000000003':
                  return 'B'
               else:
                  return 'M'
            elif obj[2] == 'Less_0.05418':
               # {"feature": "area_worst", "instances": 2, "metric_value": 0.5, "depth": 5}
               if obj[1] == 'Less_1320.5':
                  return 'M'
               else:
                  return 'M'
            elif obj[2] == 'Less_0.04877':
               return 'B'
            else:
               return 'M'
         elif obj[5] == 'Greater_14.370000000000001':
            # {"feature": "concave_points_mean", "instances": 4, "metric_value": 0.3333, "depth": 4}
            if obj[2] == 'Greater_0.05418':
               # {"feature": "area_worst", "instances": 3, "metric_value": 0.4444, "depth": 5}
               if obj[1] == 'Less_1320.5':
                  return 'B'
               else:
                  return 'M'
            elif obj[2] == 'Less_0.04877':
               return 'B'
            else:
               return 'M'
         elif obj[5] == 'Less_12.855':
            return 'M'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[0] == 'Greater_17.0':
      # {"feature": "concave_points_mean", "instances": 184, "metric_value": 0.0698, "depth": 2}
      if obj[2] == 'Greater_0.05418':
         # {"feature": "concave_points_worst", "instances": 161, "metric_value": 0.0232, "depth": 3}
         if obj[3] == 'Greater_0.1611':
            return 'M'
         elif obj[3] == 'Less_0.1611':
            # {"feature": "area_worst", "instances": 25, "metric_value": 0.0738, "depth": 4}
            if obj[1] == 'Less_1320.5':
               # {"feature": "radius_mean", "instances": 13, "metric_value": 0.1399, "depth": 5}
               if obj[5] == 'Greater_14.370000000000001':
                  return 'M'
               elif obj[5] == 'Less_14.370000000000001':
                  return 'M'
               else:
                  return 'M'
            elif obj[1] == 'Greater_1431.0':
               return 'M'
            elif obj[1] == 'Less_1431.0':
               return 'M'
            else:
               return 'M'
         elif obj[3] == 'Less_0.14205':
            # {"feature": "area_worst", "instances": 11, "metric_value": 0.1591, "depth": 4}
            if obj[1] == 'Less_1320.5':
               # {"feature": "concavity_mean", "instances": 8, "metric_value": 0.2188, "depth": 5}
               if obj[4] == 'Less_0.2096':
                  return 'M'
               else:
                  return 'M'
            elif obj[1] == 'Greater_1431.0':
               return 'M'
            elif obj[1] == 'Less_1431.0':
               return 'M'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[2] == 'Less_0.04877':
         # {"feature": "concavity_mean", "instances": 18, "metric_value": 0.4444, "depth": 3}
         if obj[4] == 'Less_0.2096':
            # {"feature": "concave_points_worst", "instances": 16, "metric_value": 0.4667, "depth": 4}
            if obj[3] == 'Less_0.14205':
               # {"feature": "radius_mean", "instances": 15, "metric_value": 0.4571, "depth": 5}
               if obj[5] == 'Greater_14.370000000000001':
                  return 'B'
               elif obj[5] == 'Less_14.370000000000001':
                  return 'M'
               else:
                  return 'M'
            elif obj[3] == 'Less_0.1611':
               return 'M'
            else:
               return 'M'
         elif obj[4] == 'Less_0.034460000000000005':
            return 'M'
         else:
            return 'M'
      elif obj[2] == 'Less_0.05418':
         return 'M'
      elif obj[2] == 'Less_0.02388':
         return 'M'
      else:
         return 'M'
   elif obj[0] == 'Less_12.89':
      # {"feature": "concave_points_worst", "instances": 136, "metric_value": 0.011, "depth": 2}
      if obj[3] == 'Less_0.14205':
         return 'B'
      elif obj[3] == 'Less_0.1611':
         # {"feature": "concavity_mean", "instances": 4, "metric_value": 0.25, "depth": 3}
         if obj[4] == 'Less_0.2096':
            # {"feature": "concave_points_mean", "instances": 2, "metric_value": 0.0, "depth": 4}
            if obj[2] == 'Greater_0.05418':
               return 'M'
            elif obj[2] == 'Less_0.04877':
               return 'B'
            else:
               return 'M'
         elif obj[4] == 'Greater_0.26385000000000003':
            return 'B'
         elif obj[4] == 'Less_0.26385000000000003':
            return 'B'
         else:
            return 'M'
      elif obj[3] == 'Greater_0.1611':
         return 'B'
      else:
         return 'M'
   elif obj[0] == 'Less_17.0':
      # {"feature": "concave_points_worst", "instances": 25, "metric_value": 0.3, "depth": 2}
      if obj[3] == 'Less_0.14205':
         # {"feature": "concave_points_mean", "instances": 20, "metric_value": 0.2386, "depth": 3}
         if obj[2] == 'Less_0.04877':
            # {"feature": "radius_mean", "instances": 11, "metric_value": 0.2182, "depth": 4}
            if obj[5] == 'Greater_14.370000000000001':
               return 'B'
            elif obj[5] == 'Less_14.370000000000001':
               # {"feature": "concavity_mean", "instances": 5, "metric_value": 0.4, "depth": 5}
               if obj[4] == 'Less_0.2096':
                  return 'M'
               elif obj[4] == 'Less_0.034460000000000005':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[2] == 'Less_0.05418':
            # {"feature": "radius_mean", "instances": 4, "metric_value": 0.25, "depth": 4}
            if obj[5] == 'Greater_14.370000000000001':
               # {"feature": "area_worst", "instances": 2, "metric_value": 0.5, "depth": 5}
               if obj[1] == 'Less_1320.5':
                  return 'M'
               else:
                  return 'M'
            elif obj[5] == 'Less_14.370000000000001':
               return 'M'
            else:
               return 'M'
         elif obj[2] == 'Less_0.02388':
            return 'B'
         elif obj[2] == 'Greater_0.05418':
            return 'B'
         else:
            return 'M'
      elif obj[3] == 'Greater_0.1611':
         return 'M'
      elif obj[3] == 'Less_0.1611':
         return 'M'
      else:
         return 'M'
   else:
      return 'M'
