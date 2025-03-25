<?php
session_start();

$output = shell_exec($command);

$response = json_decode($output, true);
echo "back in index.php burgman green \n";
echo $output;

if(trim($output) == "succeeded") {

 
  echo "PYTHON SUCCESS"; 
}    
// Check the response from the Python script
?>

<!doctype html>
<html lang="en" data-bs-theme="auto">
  <head>
    <title>CSCI 375</title>
  </head>
  <body class="text-center">
    <main class="form-signin w-100 m-auto">
      <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
        <h1 class="h3 mb-3 fw-normal">TRASH PANDAS CALCULATOR</h1>

        <div>        
          <a href="http://localhost:8080/~griffitb/csci375/income" class="btn btn-lg btn-primary w-100 mb-2">INCOMEsssss</a>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit"></button>
        <p class="mt-5 mb-3 text-body-secondary">&copy; TRASHcan PANDAS INC - 2025</p>
      </form>
    </main>
  </body>
</html>

<?php
$stmt = null;
$dbh = null;
?>
