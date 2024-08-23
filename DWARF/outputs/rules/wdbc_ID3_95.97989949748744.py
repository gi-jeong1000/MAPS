def findDecision(obj): #obj[0]: perimeter_worst, obj[1]: concave_points_worst, obj[2]: radius_worst, obj[3]: area_worst
   # {"feature": "perimeter_worst", "instances": 171, "metric_value": 0.9581, "depth": 1}
   if obj[0] == 'Less_91.695':
      # {"feature": "concave_points_worst", "instances": 61, "metric_value": 0.1207, "depth": 2}
      if obj[1] == 'Less_0.1137':
         return 'B'
      elif obj[1] == 'Less_0.059054999999999996':
         return 'B'
      elif obj[1] == 'Less_0.15505':
         # {"feature": "radius_worst", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[2] == 'Less_18.895':
            # {"feature": "area_worst", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Less_696.05':
               return 'B'
            else:
               return 'M'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[0] == 'Less_116.55000000000001':
      # {"feature": "concave_points_worst", "instances": 60, "metric_value": 0.7838, "depth": 2}
      if obj[1] == 'Less_0.1137':
         # {"feature": "area_worst", "instances": 30, "metric_value": 0.469, "depth": 3}
         if obj[3] == 'Less_696.05':
            # {"feature": "radius_worst", "instances": 16, "metric_value": 0.3373, "depth": 4}
            if obj[2] == 'Less_18.895':
               return 'B'
            else:
               return 'M'
         elif obj[3] == 'Greater_696.05':
            # {"feature": "radius_worst", "instances": 14, "metric_value": 0.5917, "depth": 4}
            if obj[2] == 'Less_18.895':
               return 'B'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[1] == 'Less_0.15505':
         # {"feature": "area_worst", "instances": 19, "metric_value": 0.8997, "depth": 3}
         if obj[3] == 'Greater_696.05':
            # {"feature": "radius_worst", "instances": 14, "metric_value": 0.9852, "depth": 4}
            if obj[2] == 'Less_18.895':
               return 'B'
            else:
               return 'M'
         elif obj[3] == 'Less_696.05':
            return 'B'
         else:
            return 'M'
      elif obj[1] == 'Greater_0.15505':
         # {"feature": "area_worst", "instances": 6, "metric_value": 0.65, "depth": 3}
         if obj[3] == 'Greater_696.05':
            return 'M'
         elif obj[3] == 'Less_696.05':
            return 'B'
         else:
            return 'M'
      elif obj[1] == 'Less_0.059054999999999996':
         return 'B'
      else:
         return 'M'
   elif obj[0] == 'Less_167.5':
      return 'M'
   elif obj[0] == 'Greater_167.5':
      return 'M'
   else:
      return 'M'
