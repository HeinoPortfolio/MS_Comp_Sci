#  Author: Matthew Heino
#  Course: DSCI 605 Data Visualization
#
#  Purpose: Programming basic line plot with combined plotly and shiny
# 

#  Load the required libraries 
library(tidyverse)
library(plotly)
library(shiny)
library(readxl)

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# Load the data set
crime_data_df <- readxl::read_xlsx("Sampledata2.xlsx")

# Inspect the data set
glimpse(crime_data_df)

# Create the inputs for the app.
crime_ui <- fluidPage(
  
  # Create the input for the State
  selectInput(inputId= "inputState", 
              label= "Select State",
              choices= unique(crime_data_df$State),
              selected= "Alabama",
              multiple= FALSE 
  ),
  plotlyOutput(outputId= "outState"),
  
  # Create the input for the Year
  selectInput(inputId= "inputYear", 
              label= "Select Year",
              choices= unique(crime_data_df$Year),
              selected= "2007",
              multiple= FALSE 
  ),
  plotlyOutput(outputId= "outYear")
  
)


# Create the server object
crime_server <- function(input, output, ...){

# Create the state output
  output$outState <- renderPlotly({
    plot_ly(data=crime_data_df, x= ~as.factor(Year), y= ~CrimeRate, color= ~State ) %>%
      filter(State %in% input$inputState) %>%
      add_markers() %>%
      group_by(State) %>%
      add_lines() %>%
      layout(title="Crime Rate by Year",  
             xaxis=list(title= "Year"),
             yaxis=list(title="Crime Rate Per 100,000 People"))})
  
# Create the Year histogram output  
 output$outYear <- renderPlotly({
   plot_ly(data= crime_data_df, x= ~CrimeRate, nbinsx= 6, name="Crime Rate") %>%
     filter(Year %in% input$inputYear)  %>%
     add_histogram(marker = list(color = "grey",line = list(color = "black",
                                                            width = 2))) %>%
     layout(title="Crime Rate Per 100,000 People",
            yaxis=list(title = "Count"),
            xaxis=list(title = "Crime RATEEEE")) %>%
   layout(showlegend=TRUE)
 })
}

shinyApp(crime_ui, crime_server)
