<?php
$host = 'dolphin'; 
$user = 'csci375team6';
$password = '3jni3edn';
$database = 'csci375team6_povertycalculator';

// Connect to MariaDB
$conn = new mysqli($host, $user, $password, $database);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Update income table if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['update'])) {
    $id = $_POST['id'];
    $income = $_POST['income'];
    $liabilities = $_POST['liabilities'];
    $obligations = $_POST['obligations'];

    $sql = "UPDATE income SET income = ?, liabilities = ?, obligations = ? WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("iiii", $income, $liabilities, $obligations, $id);
    $stmt->execute();
}

// Fetch income data with associated user's first name
$sql = "SELECT income.id, users.firstName, income.income, income.liabilities, income.obligations 
        FROM income 
        JOIN users ON income.ownerId = users.id";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Income Table</title>
    <style>
        table {
            width: 60%;
            border-collapse: collapse;
        }
        th, td {
            padding: 8px;
            text-align: center;
            border: 1px solid black;
        }
        form {
            display: inline;
        }
    </style>
</head>
<body>
    <h2>Income Table</h2>
    <table>
        <tr>
            <th>First Name</th>
            <th>Income</th>
            <th>Liabilities</th>
            <th>Obligations</th>
            <th>Action</th>
        </tr>

        <?php while ($row = $result->fetch_assoc()): ?>
        <tr>
            <form method="post">
                <td><?php echo htmlspecialchars($row['firstName']); ?></td>
                <td><input type="number" name="income" value="<?php echo $row['income']; ?>"></td>
                <td><input type="number" name="liabilities" value="<?php echo $row['liabilities']; ?>"></td>
                <td><input type="number" name="obligations" value="<?php echo $row['obligations']; ?>"></td>
                <td>
                    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                    <input type="submit" name="update" value="Update">
                </td>
            </form>
        </tr>
        <?php endwhile; ?>
    </table>
</body>
</html>

<?php
$conn->close();
?>
