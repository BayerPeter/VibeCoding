from app import create_app, db
from app.models import Complaint, Report
from datetime import datetime

def create_test_data():
    app = create_app()
    
    with app.app_context():
        try:
            # Clear existing data
            db.session.query(Report).delete()
            db.session.query(Complaint).delete()
            db.session.commit()
            print("Cleared existing data")
            
            # Create test complaints
            complaints = [
                Complaint(
                    product='Test Medicine A',
                    batch_number='BATCH001',
                    description='Quality issue with packaging',
                    status='pending',
                    submission_date=datetime.utcnow()
                ),
                Complaint(
                    product='Test Medicine B',
                    batch_number='BATCH002',
                    description='Product efficacy concern',
                    status='in_review',
                    submission_date=datetime.utcnow()
                )
            ]
            
            for complaint in complaints:
                db.session.add(complaint)
            db.session.commit()
            print(f"Created {len(complaints)} test complaints")
            
            # Create test reports
            reports = []
            for complaint in complaints:
                report = Report(
                    complaint_id=complaint.id,
                    version=1,
                    status='draft',
                    sample_examination='Initial examination completed',
                    retention_sample_check='Sample check pending',
                    manufacturing_review='Manufacturing records under review',
                    root_cause_analysis='Investigation in progress',
                    similar_complaints='No similar complaints found',
                    risk_classification='low',
                    conclusion='Initial assessment pending',
                    root_cause_category='Quality Control',
                    root_cause_subcategory='Packaging',
                    defect_origin='Manufacturing',
                    defect_category='Minor',
                    defect_impact='Limited to single batch',
                    capa_required=True,
                    capa_actions='To be determined',
                    effectiveness_check='Pending implementation',
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow()
                )
                reports.append(report)
                
            for report in reports:
                db.session.add(report)
            db.session.commit()
            print(f"Created {len(reports)} test reports")
            
            print("\nTest data summary:")
            print(f"Complaints: {Complaint.query.count()}")
            print(f"Reports: {Report.query.count()}")
            print(f"Draft Reports: {Report.query.filter_by(status='draft').count()}")
            
        except Exception as e:
            print(f"Error creating test data: {e}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    create_test_data()
