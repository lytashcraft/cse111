import pytest
from missionary_schedule import schedule, cancel_appointment, view_appointments, generate_weekly_report, appointments

@pytest.fixture(autouse=True)
def reset_appointments():
    """Reset the appointments list before each test."""
    appointments.clear()

def test_schedule_appointment():
    """Test scheduling a valid appointment."""
    schedule('Visit', '15/10/2024', '10:00', 'John Doe', '1234567890', '123 Main St')
    assert len(appointments) == 1, "Expected 1 appointment to be scheduled."
    assert appointments[0]['name'] == 'John Doe', "Expected appointment name to be 'John Doe'."
    assert appointments[0]['date'] == '15/10/2024', "Expected appointment date to be '15/10/2024'."
    assert appointments[0]['time'] == '10:00', "Expected appointment time to be '10:00'."

def test_schedule_appointment_conflict():
    """Test that scheduling a conflicting appointment is not allowed."""
    schedule('Visit', '15/10/2024', '10:00', 'John Doe', '1234567890', '123 Main St')
    schedule('Visit', '15/10/2024', '10:00', 'Jane Doe', '0987654321', '456 Main St')
    assert len(appointments) == 1, "Expected no new appointment to be added due to conflict."


def test_view_appointments(capfd):
    """Test viewing scheduled appointments."""
    schedule('Visit', '15/10/2024', '10:00', 'John Doe', '1234567890', '123 Main St')
    view_appointments()  # This will print the appointments
    captured = capfd.readouterr()  # Capture the output
    assert "Visit - Date: 15/10/2024, Time: 10:00, Name: John Doe" in captured.out, "Expected appointment to be displayed."

def test_generate_weekly_report(monkeypatch):
    """Test generating a weekly report for scheduled appointments."""
    from io import StringIO
    import sys

    output = StringIO()
    monkeypatch.setattr(sys, 'stdout', output)

    schedule('Visit', '15/10/2024', '10:00', 'John Doe', '1234567890', '123 Main St')
    generate_weekly_report()
    
    # Check if the report contains the appointment
    report_content = output.getvalue()
    assert 'Visit - Date: 15/10/2024, Time: 10:00, Name: John Doe' in report_content, "Expected report to contain the scheduled appointment."

def test_schedule_appointment_in_past():
    """Test that appointments cannot be scheduled in the past."""
    schedule('Visit', '15/10/2023', '10:00', 'John Doe', '1234567890', '123 Main St')
    assert len(appointments) == 0, "Expected no appointments to be scheduled for a past date."

def test_cancel_appointment():
    """Test canceling a scheduled appointment."""

    # Cancel the scheduled appointment
    cancel_appointment('15/10/2024', '10:00')
    
    # Assert that the appointment list is empty after cancellation
    assert len(appointments) == 0, "Expected appointment to be canceled."

def test_cancel_nonexistent_appointment():
    """Test attempting to cancel an appointment that doesn't exist."""
    # Attempting to cancel a non-existent appointment
    cancel_appointment('15/10/2024', '10:00')  # Should not raise an error
    


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
