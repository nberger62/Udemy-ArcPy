import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\ArcGISData\UdemyArcPy_Course_ArcProjects\IntorductiontoArcPy\IntorductiontoArcPy.gdb"

#  fc = r"D:\ArcGISData\ArcDataTutorial\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"D:\ArcGISData\ArcDataTutorial\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print_message("{0} has {1} feature(s)".format(fc, numFeats))

#  arcpy.Select_analysis(fc, "Egypt", "NAME = 'Egypt'")

print_message("Script Completed!")

# Label class properties for census population function
# def FindLabel ([NAME],[LASTCENSUS],[POP_EST]):
#     text = "{0}\n{1} census:\n{2:,}".format([NAME],[LASTCENSUS],int([POP_EST]))
#     return text

# Setting up a new field to calculate GDP per person in the country based on census data
#def set_text(pop,dgp):
    #if pop == 0 or gdp == 0:
        #text = "0"
    #else:
        #text = "GDPPP: US${0:,}".format(int((gdp * 1000000) / pop))
    #return text