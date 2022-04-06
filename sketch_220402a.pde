import processing.svg.*;
Table table;
float skala = 1;

void setup() {
 size(1900, 800); 
 background(255, 255, 242);
}

void draw() {
 beginRecord(SVG, "./circles.svg");
 table = loadTable("./data_preparation/data/edited.csv", "header");
 translate(100,0);

 int i, z, k, row_count;
 row_count = 0;
 for (k=1; k<8; k++) {
    translate(0,100);
    i = 0;
    for(z=1; z<49; z++){
   
      int mood1 = table.getInt(row_count, "mood1");
      String category1 = table.getString(row_count, "kategory1");
      colorFill(category1, i, mood1);
       
      int mood2 = table.getInt(row_count, "mood2");
      String category2 = table.getString(row_count, "kategory2");
      colorStroke(category2, i, mood2);
      
      i++;
      row_count++;
      if(row_count == table.getRowCount()){
       break;
      }
    }
   }
   endRecord();
}

void colorFill(String category, int i, int mood1){
  noStroke();
  switch (category){
    case "sleep":
      fill(0, 0, 0, 70);
      break;
    case "hygiene":
      fill(154, 247, 199, 70);
      break;
    case "food":
      fill(255, 205, 210, 70);
      break;
    case "onTheWay":
      fill(224, 224, 224, 70);
      break;
    case "Study":
      fill(178, 235, 242, 70);
      break;  
    case "freeTime":
      fill(209, 196, 233, 70);
      break;  
  }
  ellipse(i*35, 0, mood1*skala + 10, mood1*skala + 10);
}


void colorStroke(String category, int i, int mood2){
  noFill();
  strokeWeight(2);
  switch (category){
    case "sleep":
      stroke(0, 0, 0);
      break;
    case "hygiene":
      stroke(53, 240, 143);
      break;
    case "food":
      stroke(255, 23, 68);
      break;
    case "onTheWay":
      stroke(158,158,158);
      break;
    case "Study":
      stroke(0, 184, 212);
      break;  
    case "freeTime":
      stroke(170, 0, 255);
      break;  
  }

  ellipse(i*35, 0, mood2*mood2 + 5, mood2*mood2 + 5);
}
