<?php
session_start(); 
if(!isset($_SESSION['admin_id'])) 
{
  session_destroy();
  header("location:../Logout.php");    
}
require '../Classes/init.php';
 $func = new Operation(); 


  $task_id=$_POST['task_id']; 
  $status=$_POST['val'];  

 

  $result = $func->update('task',array("task_display ='".$status."'"),"task_id ='" . $task_id . "'");  

  if ($result === TRUE) 
  { 
    
  } 

?>