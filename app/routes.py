from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import func
from app import db, cache
from app.models import Farmer, Feed, Medicine, Equipment, MilkSales, MilkProduction, MaintenanceCosts
from datetime import datetime, timedelta
import logging

bp = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@bp.route('/')
def home():
    return render_template('home.html')

# Route to render the analysis page
@bp.route('/analysis')
def analysis():
    farmers = Farmer.query.all()
    return render_template('analysis.html', farmers=farmers)

# Route to fetch analysis data for a specific farmer
@bp.route('/fetch_analysis_data', methods=['POST'])
def fetch_analysis_data():
    farmer_id = request.form.get('farmer_id')
    if not farmer_id:
        return jsonify({'error': 'No farmer selected'})

    # Fetch data for Milk Production, Milk Sales, Maintenance Costs, Feeds, Medicine, Equipment
    milk_production_data = MilkProduction.query.filter_by(farmer_id=farmer_id).all()
    milk_sales_data = MilkSales.query.filter_by(farmer_id=farmer_id).all()
    maintenance_costs_data = MaintenanceCosts.query.filter_by(farmer_id=farmer_id).all()
    feeds_data = Feed.query.filter_by(farmer_id=farmer_id).all()
    medicine_data = Medicine.query.filter_by(farmer_id=farmer_id).all()
    equipment_data = Equipment.query.filter_by(farmer_id=farmer_id).all()

    # Prepare data for charts
    milk_production_labels = [prod.date.strftime('%Y-%m-%d') for prod in milk_production_data]
    milk_production_values = [prod.milk_produced for prod in milk_production_data]

    milk_sales_labels = [sales.date.strftime('%Y-%m-%d') for sales in milk_sales_data]
    milk_sales_values = [sales.revenue for sales in milk_sales_data]

    maintenance_costs_labels = [cost.date.strftime('%Y-%m-%d') for cost in maintenance_costs_data]
    maintenance_costs_values = [cost.cost for cost in maintenance_costs_data]

    # No date attribute for feeds, medicine, and equipment
    feeds_labels = ['Feed'] * len(feeds_data)
    feeds_costs = [feed.cost * feed.quantity for feed in feeds_data]

    medicine_labels = ['Medicine'] * len(medicine_data)
    medicine_costs = [med.cost * med.quantity for med in medicine_data]

    equipment_labels = ['Equipment'] * len(equipment_data)
    equipment_costs = [equip.cost * equip.quantity for equip in equipment_data]

    # Calculate total expenses
    total_feeds_cost = sum(feeds_costs)
    total_medicine_cost = sum(medicine_costs)
    total_equipment_cost = sum(equipment_costs)
    total_expenses = total_feeds_cost + total_medicine_cost + total_equipment_cost

    # Calculate profit/loss
    total_milk_sales = sum(milk_sales_values)
    total_milk_production_costs = sum(milk_production_values) + sum(maintenance_costs_values) + total_expenses
    profit_loss = total_milk_sales - total_milk_production_costs

    # Example: Calculate summary statistics
    milk_production_total = sum(milk_production_values)
    milk_sales_total = sum(milk_sales_values)
    maintenance_costs_total = sum(maintenance_costs_values)

    summary_statistics = {
        'milk_production_total': milk_production_total,
        'milk_sales_total': milk_sales_total,
        'maintenance_costs_total': maintenance_costs_total,
        'total_feeds_cost': total_feeds_cost,
        'total_medicine_cost': total_medicine_cost,
        'total_equipment_cost': total_equipment_cost,
        'total_expenses': total_expenses,
        'profit_loss': profit_loss
    }

    return jsonify({
        'milk_production_labels': milk_production_labels,
        'milk_production_values': milk_production_values,
        'milk_sales_labels': milk_sales_labels,
        'milk_sales_values': milk_sales_values,
        'maintenance_costs_labels': maintenance_costs_labels,
        'maintenance_costs_values': maintenance_costs_values,
        'feeds_labels': feeds_labels,
        'feeds_costs': feeds_costs,
        'medicine_labels': medicine_labels,
        'medicine_costs': medicine_costs,
        'equipment_labels': equipment_labels,
        'equipment_costs': equipment_costs,
        'summary_statistics': summary_statistics
    })

@bp.route('/forecast_profit_loss', methods=['POST'])
def forecast_profit_loss():
    farmer_id = request.form.get('farmer_id')
    if not farmer_id:
        return jsonify({'error': 'No farmer selected'})

    # Fetch relevant data for forecasting (e.g., milk sales, expenses, etc.)
    # Perform forecasting calculation (e.g., using regression or moving average)

    # For simplicity, let's assume a basic linear projection
    summary_statistics = {
        'profit_loss': 10000  # Example value for projected profit/loss
    }

    return jsonify({
        'projected_profit_loss': summary_statistics['profit_loss']
    })
