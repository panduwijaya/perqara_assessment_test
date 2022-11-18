def queen(n, k, r_q, c_q, obstacles):
    # Initialize all of the distances for the queen without obstacles
    dtr = n - c_q # distance to the right of queen
    dtl = c_q - 1 # distance to the left of queen
    daq = n - r_q # distance above the queen
    dbq = r_q - 1 # distance below the queen
    # Diagonal distance is the shortest distance between horizontal or vertical
    diag45 = dtr if (dtr<daq) else daq
    diag135 = dtr if (dtr<dbq) else dbq
    diag225 = dtl if (dtl<dbq) else dbq
    diag315 = dtl if (dtl<daq) else daq
    
    # Iterate obstacle and compare it with each value
    for obs in obstacles:
        # Conditions
        xAxis = True if(obs[1] > c_q) else False # True if obs on the right of the queen
        yAxis = True if(obs[0] > r_q) else False # True if obs above the queen
        # The obs is diagonalically aligned if the diff between x axis == diff between y axis
        diag_check = True if (abs(r_q - obs[0])==abs(c_q - obs[1])) else False
        
        # If the obs on the same row as the queen
        if(r_q == obs[0]):
            # Calculate the horizontal difference
            col_dif = abs(obs[1] - c_q)-1
            # Change horizontal position if the value is smaller than previous value
            if(xAxis and dtr>col_dif):
                dtr = col_dif
            elif(dtl>col_dif):
                dtl = col_dif
        
        # Do the same if obs on the sam column as the queen
        if(c_q == obs[1]):
            row_dif = abs(obs[0] - r_q)-1
            if(yAxis and daq>row_dif):
                daq = row_dif
            elif(dbq>row_dif):
                dbq = row_dif
        
        # If the obs diagonalically aligned
        if(diag_check):
            # Calculate the difference
            diag_dif = abs(r_q - obs[0]) - 1
            # Change position value if the diff is smaller than previous value
            if(xAxis and yAxis and diag_dif < diag45):
                diag45 = diag_dif
            elif(xAxis and not yAxis and diag_dif < diag135):
                diag135 = diag_dif
            elif(not xAxis and not yAxis and diag_dif < diag225):
                diag225 = diag_dif
            elif(not xAxis and yAxis and diag_dif < diag315):
                diag315 = diag_dif
                
    # Return the sum of all positions    
    return dtr + dtl + daq + dbq + diag45 + diag135 + diag225 + diag315 