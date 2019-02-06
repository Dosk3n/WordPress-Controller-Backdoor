<?php
// Note: If the table prefix has been changed from default you will need to change it in the locations of this code

// Nothing is to happen without an option
if(isset($_GET['m'])) {
	//file.php?m={mode} - This will select the required 
    $mode = $_GET['m'];
	
	// This is the "menu"
	switch ($mode) {
		case "gu":
			// Get Users
			GetUsersCheck();
			break;
		case "sph":
			// Change Password Hash
			ChangeHashCheck();
			break;
	}	
}

function GetUsersCheck(){
	if(isset($_GET['dbh']) && isset($_GET['dbn']) && isset($_GET['dbu']) && isset($_GET['dbp'])) {
		$dbhost = $_GET['dbh'];
		$dbname = $_GET['dbn'];
		$dbuser = $_GET['dbu'];
		$dbpass = $_GET['dbp'];
		GetUsers($dbhost, $dbname, $dbuser, $dbpass);
	}
}

function ChangeHashCheck(){
	if(isset($_GET['dbh']) && isset($_GET['dbn']) && isset($_GET['dbu']) && isset($_GET['dbp']) && isset($_GET['uid']) && isset($_GET['pwh'])) {
		$dbhost = $_GET['dbh'];
		$dbname = $_GET['dbn'];
		$dbuser = $_GET['dbu'];
		$dbpass = $_GET['dbp'];
		$userid = $_GET['uid'];
		$pwhash = $_GET['pwh'];
		ChangeHash($dbhost, $dbname, $dbuser, $dbpass, $userid, $pwhash);
	}
}

function ChangeHash($dbhost, $dbname, $dbuser, $dbpass, $userid, $pwhash){
	$db_prefix = "wp_"; // wp_ is the default wordpress prefix - only change if needed
	$sql = "UPDATE " . $db_prefix . "users SET user_pass='" . $pwhash . "' WHERE ID=" . $userid;
	
	// Create connection
	$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	if ($conn->query($sql) === TRUE) {
		echo "true";
	} else {
		echo "false";
	}

	$conn->close();
}

function GetUsers($dbhost, $dbname, $dbuser, $dbpass){
	$db_prefix = "wp_"; // wp_ is the default wordpress prefix - only change if needed
	$sql = "SELECT * FROM " . $db_prefix . "users";
	
	$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 
	$result = $conn->query($sql);
	$data = [];
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			$d = array("id"=>$row["ID"], "user"=>$row["user_login"], "pass"=>$row["user_pass"], "email"=>$row["user_email"]);
			array_push($data, $d);
		}
	} else {
		echo "0 results";
	}
	$conn->close();
	$json = json_encode($data);
	echo $json;
}

?>