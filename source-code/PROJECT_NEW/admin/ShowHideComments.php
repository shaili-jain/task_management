<?php
 session_start(); 
if(!isset($_SESSION['admin_id']))
{
  session_destroy();
  header("location:../Logout.php");    
}
 require '../Classes/init.php';
 $func = new Operation();

	$comment_id=$_POST['comment_id'];	
	$status=$_POST['val'];

	 
	$result = $func->update('comments',array("comment_display ='".$status."'"),"comment_id ='" . $comment_id . "'");
	if ($result === TRUE) 
	{	
	  
	}	

?>