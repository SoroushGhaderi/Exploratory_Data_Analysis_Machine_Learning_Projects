def height_notation(plot_name , coordinator , dataframe , color="white", percent=False, height_type=int):
    """
    Args:
        plot_name ([matplotlib plot]): 
            name of plot
        coordinator ([integer]): [description]
        dataframe ([type]): [description]
        color (str, optional): [description]. Defaults to "white".
        percent (bool, optional): [description]. Defaults to False.
        height_type ([type], optional): [description]. Defaults to int.
    """
    total = len(dataframe)
    for p in plot_name.patches:
        height = p.get_height().round(2)
        text = str(height_type(height))
        if percent == True:
            plot_name.text(p.get_x() + p.get_width() / 2 , height + coordinator , text + ' | ' + str(height * 100 // total) + '%' , ha = 'center', color="white")
        else:
            plot_name.text(p.get_x() + p.get_width() / 2 , height + coordinator , text , ha = 'center', color=color)